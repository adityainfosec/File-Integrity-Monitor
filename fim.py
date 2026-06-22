#!/usr/bin/env python3
"""
File Integrity Monitor (FIM) - Improved Version
Author: Aditya (refactored)
Description: Secure file integrity monitoring using SHA-256 + SQLite
"""

import os
import sys
import hashlib
import argparse
import sqlite3
from pathlib import Path
from datetime import datetime
import logging

# ---------------- Logging Setup ----------------
logging.basicConfig(
    level=logging.INFO,
    format="[*] %(message)s"
)

# ---------------- Core Class ----------------
class FileIntegrityMonitor:
    def __init__(self, db_file="fim.db"):
        self.db_file = db_file
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()
        self._init_db()

    def _init_db(self):
        """Initialize SQLite table"""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS files (
                path TEXT PRIMARY KEY,
                hash TEXT NOT NULL,
                last_modified TEXT NOT NULL
            )
        """)
        self.conn.commit()

    # ---------------- Hash Function ----------------
    def calculate_hash(self, filepath):
        sha256 = hashlib.sha256()
        try:
            with open(filepath, "rb") as f:
                while chunk := f.read(4096):
                    sha256.update(chunk)
            return sha256.hexdigest()
        except Exception as e:
            logging.warning(f"Cannot read {filepath}: {e}")
            return None

    # ---------------- Baseline ----------------
    def baseline(self, target_path):
        target = Path(target_path)

        if not target.exists():
            logging.error("Path does not exist")
            return

        logging.info(f"Creating baseline for: {target_path}")

        self.cursor.execute("DELETE FROM files")  # reset baseline

        if target.is_file():
            files = [target]
        else:
            files = [f for f in target.rglob("*") if f.is_file()]

        count = 0

        for file in files:
            hash_val = self.calculate_hash(str(file))
            if not hash_val:
                continue

            rel_path = str(file.relative_to(target))

            self.cursor.execute("""
                INSERT OR REPLACE INTO files (path, hash, last_modified)
                VALUES (?, ?, ?)
            """, (
                rel_path,
                hash_val,
                datetime.now().isoformat()
            ))

            logging.info(f"Added: {rel_path}")
            count += 1

        self.conn.commit()
        logging.info(f"Baseline completed: {count} files stored")

    # ---------------- Check Integrity ----------------
    def check(self, target_path):
        target = Path(target_path)

        if not target.exists():
            logging.error("Path does not exist")
            return

        logging.info(f"Checking integrity: {target_path}")

        self.cursor.execute("SELECT * FROM files")
        rows = self.cursor.fetchall()

        if not rows:
            logging.error("No baseline found. Run baseline first.")
            return

        db_data = {row[0]: row[1] for row in rows}

        current_files = {
            str(f.relative_to(target)): f
            for f in target.rglob("*") if f.is_file()
        }

        modified = []
        deleted = []
        added = []

        # check modified + deleted
        for path, old_hash in db_data.items():
            full_path = target / path

            if not full_path.exists():
                deleted.append(path)
                continue

            new_hash = self.calculate_hash(str(full_path))

            if new_hash and new_hash != old_hash:
                modified.append(path)

        # check new files
        for path in current_files:
            if path not in db_data:
                added.append(path)

        # ---------------- Report ----------------
        print("\n" + "="*50)
        print("INTEGRITY REPORT")
        print("="*50)

        if not modified and not deleted and not added:
            print("[✓] No changes detected")
            return

        if modified:
            print("\n[!] Modified Files:")
            for f in modified:
                print(" -", f)

        if deleted:
            print("\n[!] Deleted Files:")
            for f in deleted:
                print(" -", f)

        if added:
            print("\n[!] New Files:")
            for f in added:
                print(" +", f)

    # ---------------- Close DB ----------------
    def close(self):
        self.conn.close()


# ---------------- CLI ----------------
def main():
    parser = argparse.ArgumentParser(description="File Integrity Monitor (FIM)")

    parser.add_argument("action", choices=["baseline", "check"])
    parser.add_argument("path", help="Target directory/file")

    args = parser.parse_args()

    fim = FileIntegrityMonitor()

    try:
        if args.action == "baseline":
            fim.baseline(args.path)

        elif args.action == "check":
            fim.check(args.path)

    except KeyboardInterrupt:
        print("\n[!] Interrupted")

    finally:
        fim.close()


if __name__ == "__main__":
    main()
