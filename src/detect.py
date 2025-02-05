import json

import random
import logging
import sqlite3
import pandas as pd

from PIL import Image as PILImage
import IPython.display as display
from ultralytics import YOLO

# Setting up logging
logging.basicConfig(level=logging.INFO)


def detect_objects(image_path):
    """
    Detects objects in an image using YOLOv8.

    Args:
        image_path: The path to the image file.

    Returns:
        A list of dictionaries, where each dictionary represents a detected object
        and contains information like bounding box coordinates, class, and confidence.
        Returns None if the image is not found or an error occurs.
    """
    try:
        model = YOLO("yolov8m.pt")  # Load a pretrained YOLOv8m model
        results = model.predict(
            source=image_path, conf=0.25
        )  # set confidence threshold

        detections = []
        for result in results:
            boxes = result.boxes
            for box in boxes:
                xyxy = box.xyxy[0].tolist()  # get bounding box coordinates
                cls = int(box.cls[0])  # get class index
                conf = float(box.conf[0])  # get confidence score

                detections.append(
                    {
                        "xmin": xyxy[0],
                        "ymin": xyxy[1],
                        "xmax": xyxy[2],
                        "ymax": xyxy[3],
                        "class": model.names[cls],
                        "confidence": conf,
                    }
                )
        return detections
    except Exception as e:
        print(f"Error detecting objects: {e}")
        return None


def detect_and_visualize(df, channel_address):
    """
    Selects a random media path for a given channel address, performs object detection,
    and visualizes the results with bounding boxes.
    """
    channel_df = df[df["channel_address"] == channel_address]
    if channel_df.empty:
        print(f"No media found for channel address: {channel_address}")
        return

    random_media_path = random.choice(channel_df["media_path"].tolist())
    print(f"Selected image: {random_media_path}")

    detections = detect_objects(random_media_path)
    if detections:
        model = YOLO("yolov8m.pt")
        results = model.predict(source=random_media_path, conf=0.25, save=True)

        # Display the image with bounding boxes
        for result in results:
            im_array = result.plot()  # This should give you a NumPy array

            # Convert the NumPy array to a PIL Image
            im_pil = PILImage.fromarray(im_array)

            # Display the image in the notebook
            display.display(im_pil)
    else:
        print("No detections found.")


def add_detections_column(connection):
    """Adds a 'detections' column to the telegram_messages table if it does not exist."""
    try:
        with connection:
            connection.execute(
                """
                ALTER TABLE telegram_messages 
                ADD COLUMN detections TEXT DEFAULT '[]';
            """
            )
        logging.info("✅ Column 'detections' added successfully.")
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e).lower():
            logging.info("ℹ️ Column 'detections' already exists. Skipping alteration.")
        else:
            logging.error(f"❌ Error adding column: {e}")
            raise


def update_detections_by_message_id(connection, df):
    """Updates the detections column for rows using message_id from the pandas dataframe."""
    try:
        with connection:
            for _, row in df.iterrows():
                detections_json = json.dumps(
                    row["detections"]
                )  # Convert list to JSON string
                connection.execute(
                    """
                    UPDATE telegram_messages 
                    SET detections = ? 
                    WHERE message_id = ?;
                """,
                    (detections_json, row["message_id"]),
                )
        logging.info("✅ Detections updated for all matching message IDs.")
    except Exception as e:
        logging.error(f"❌ Error updating detections: {e}")
        raise
