import os
import sqlite3
from dotenv import load_dotenv

# 環境変数読み込み
load_dotenv()


def migrate():
    conn = sqlite3.connect(os.getenv("DATABASE_URL"))
    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS major (
            "name" TEXT
        )
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS product_category (
            "name" TEXT
        )
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS product (
            "name" TEXT
        )
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS item (
            "name" TEXT
        )
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS devision (
            "name" TEXT
        )
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS channel (
            "name" TEXT
        )
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS level (
            "level7" TEXT,
            "level6" TEXT,
            "level5" TEXT,
            "level4" TEXT,
            "level3" TEXT
        )
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS variance_factor (
            "level7" TEXT,
            "level6" TEXT,
            "level5" TEXT,
            "level4" TEXT,
            "level3" TEXT
        )
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS pl_data (
            "Year" TEXT,
            "Quarter" TEXT,
            "Period" TEXT,
            "Major and Name" TEXT,
            "Minor Sub Product Category and Desc" TEXT,
            "Product 2" TEXT,
            "Product 1" TEXT,
            "Item Desc 1" TEXT,
            "Item Desc 2" TEXT,
            "Division Name" TEXT,
            "Channel Name" TEXT,
            "Level 1" TEXT,
            "Level 2" TEXT,
            "Level 3" TEXT,
            "Level 4" TEXT,
            "Level 5" TEXT,
            "Amt" REAL,
            "$ per Pound" REAL
        )
        """
    )


if __name__ == "__main__":
    migrate()
