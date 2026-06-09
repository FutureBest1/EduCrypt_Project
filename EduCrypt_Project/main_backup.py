import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
import threading
import time
from datetime import datetime

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class EduCryptSimulator:

    def update_timer(self):

        while self.countdown_seconds > 0:

            hours = self.countdown_seconds // 3600
            minutes = (self.countdown_seconds % 3600) // 60
            seconds = self.countdown_seconds % 60

            self.timer_label.configure(
                text=f"DECRYPTION KEY EXPIRES IN\n{hours:02}:{minutes:02}:{seconds:02}"
            )

            time.sleep(1)

            self.countdown_seconds -= 1

    def __init__(self, root):
        self.countdown_seconds = 86400
        self.root = root
        self.root.title("EduCrypt - Ransomware Simulator")
        self.root.geometry("1000x650")

        self.files = []
        self.encrypted_files = []

        self.attack_status = "Idle"
        self.threat_level = "LOW"

        self.build_ui()

    def build_ui(self):

        title = ctk.CTkLabel(
            self.root,
            text="EDUCRYPT RANSOMWARE SIMULATOR",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=15)

        dashboard = ctk.CTkFrame(self.root)
        dashboard.pack(fill="x", padx=20, pady=5)
        self.timer_label = ctk.CTkLabel(
            self.root,
            text="DECRYPTION KEY EXPIRES IN\n24:00:00",
            font=("Arial", 20, "bold"),
            text_color="orange"
        )
        self.timer_label.pack(pady=10)

        self.warning_label = ctk.CTkLabel(
            self.root,
            text="SYSTEM SECURE",
            font=("Arial", 18, "bold"),
            text_color="green"
        )
        self.warning_label.pack(pady=5)

        self.status_label = ctk.CTkLabel(
            dashboard,
            text="Attack Status: Idle",
            font=("Arial", 16, "bold")
        )
        self.status_label.pack(side="left", padx=20)

        self.threat_label = ctk.CTkLabel(
            dashboard,
            text="Threat Level: LOW",
            font=("Arial", 16, "bold"),
            text_color="green"
        )
        self.threat_label.pack(side="left", padx=20)

        top_frame = ctk.CTkFrame(self.root)
        top_frame.pack(fill="x", padx=20, pady=10)

        self.folder_label = ctk.CTkLabel(
            top_frame,
            text="No folder selected"
        )
        self.folder_label.pack(side="left", padx=10)

        select_btn = ctk.CTkButton(
            top_frame,
            text="Select Folder",
            command=self.select_folder
        )
        select_btn.pack(side="right", padx=10)

        stats_frame = ctk.CTkFrame(self.root)
        stats_frame.pack(fill="x", padx=20, pady=10)

        self.files_count = ctk.CTkLabel(
            stats_frame,
            text="Files Found: 0"
        )
        self.files_count.pack(side="left", padx=20)

        self.encrypted_count = ctk.CTkLabel(
            stats_frame,
            text="Simulated Encrypted: 0"
        )
        self.encrypted_count.pack(side="left", padx=20)

        self.progress = ctk.CTkProgressBar(self.root)
        self.progress.pack(fill="x", padx=20, pady=10)
        self.progress.set(0)

        btn_frame = ctk.CTkFrame(self.root)
        btn_frame.pack(fill="x", padx=20, pady=10)

        start_btn = ctk.CTkButton(
            btn_frame,
            text="Start Simulation",
            command=self.start_simulation
        )
        start_btn.pack(side="left", padx=10)

        recover_btn = ctk.CTkButton(
            btn_frame,
            text="Recover Files",
            command=self.recover
        )
        recover_btn.pack(side="left", padx=10)

        ransom_btn = ctk.CTkButton(
            btn_frame,
            text="Show Ransom Note",
            command=self.show_ransom_note
        )
        ransom_btn.pack(side="left", padx=10)

        report_btn = ctk.CTkButton(
            btn_frame,
            text="Generate Report",
            command=self.generate_report
        )
        report_btn.pack(side="left", padx=10)

        bottom_frame = ctk.CTkFrame(self.root)
        bottom_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.file_box = ctk.CTkTextbox(bottom_frame, width=350)
    self.file_box.pack(side="left", fill="y", padx=5, pady=5)

    self.file_box.insert(
    "end",
    "FILE STATUS\n"
)
    self.file_box.insert(
    "end",
    "=====================\n"
)

    self.log_box = ctk.CTkTextbox(bottom_frame)
    self.log_box.pack(side="right", fill="both", expand=True, padx=5, pady=5)

    def log(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_box.insert("end", f"[{timestamp}] {message}\n")
        self.log_box.see("end")

    def select_folder(self):

        folder = filedialog.askdirectory()

        if not folder:
            return

        self.folder_label.configure(text=folder)

        self.files = []

        for root, dirs, files in os.walk(folder):
            for file in files:
                self.files.append(os.path.join(root, file))

        self.files_count.configure(
            text=f"Files Found: {len(self.files)}"
        )

        self.file_box.delete("1.0", "end")

        self.file_box.insert(
        "end",
        "FILE STATUS\n"
)
        self.file_box.insert(
         "end",
         "=====================\n"
)

        for file in self.files:
            filename = os.path.basename(file)

        self.file_box.insert(
        "end",
        f"{filename}  [NORMAL]\n"
    )

        self.log(f"Scanned folder: {folder}")
        self.log(f"{len(self.files)} files discovered")

    def start_simulation(self):

        if not self.files:
            messagebox.showwarning(
                "Warning",
                "Please select a folder first."
            )
            return

        threading.Thread(
            target=self.simulate_encryption,
            daemon=True
        ).start()

    def simulate_encryption(self):

        self.encrypted_files = []

        total = len(self.files)

        self.attack_status = "Active"
        self.threat_level = "CRITICAL"

        threading.Thread(
        target=self.update_timer,
        daemon=True
        ).start()

        self.status_label.configure(
            text="Attack Status: Active"
        )

        self.warning_label.configure(
        text="SYSTEM SECURE",
        text_color="green"
)
        self.threat_label.configure(
            text="Threat Level: CRITICAL",
            text_color="red"
        )

        self.log("Attack started")
        self.log("Discovery phase completed")

        for index, file in enumerate(self.files):

            time.sleep(0.05)

            self.encrypted_files.append(file)

            filename = os.path.basename(file)

            self.file_box.insert(
            "end",
             f"{filename}  [ENCRYPTED]\n"
)

        self.file_box.see("end")

        progress = (index + 1) / total
        self.progress.set(progress)

        self.encrypted_count.configure(
        text=f"Simulated Encrypted: {len(self.encrypted_files)}"
        )

        self.log("Encryption simulation completed")
        self.log("Ransom note deployed")

        self.show_ransom_note()

    def show_ransom_note(self):

        note = ctk.CTkToplevel(self.root)
        note.title("Ransom Note")
        note.geometry("700x450")

        text = f"""
YOUR FILES HAVE BEEN ENCRYPTED

This is a cybersecurity education simulation.

No files have actually been encrypted.

The purpose of this demonstration is to
show how ransomware behaves during an attack.

Files affected:
{len(self.encrypted_files)}
        """

        label = ctk.CTkLabel(
            note,
            text=text,
            font=("Courier", 18),
            justify="left"
        )
        label.pack(pady=40, padx=20)

    def generate_report(self):

        report_name = (
            f"attack_report_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        )

        with open(report_name, "w") as report:
            report.write("EDUCRYPT INCIDENT REPORT\n")
            report.write("=" * 40 + "\n")
            report.write(f"Generated: {datetime.now()}\n")
            report.write(f"Files Found: {len(self.files)}\n")
            report.write(
                f"Simulated Encrypted: "
                f"{len(self.encrypted_files)}\n"
            )
            report.write(
                f"Threat Level: {self.threat_level}\n"
            )
            report.write(
                f"Attack Status: {self.attack_status}\n"
            )

        self.log(f"Report generated: {report_name}")

        messagebox.showinfo(
            "Report",
            f"Report saved as:\n{report_name}"
        )

    def recover(self):

        self.encrypted_files.clear()

    self.file_box.delete("1.0", "end")

    self.file_box.insert(
            "end",
            "FILE STATUS\n"
        )

    self.file_box.insert(
            "end",
            "=====================\n"
        )

    self.progress.set(0)

    self.attack_status = "Recovered"
    self.threat_level = "LOW"

    self.status_label.configure(
            text="Attack Status: Recovered"
        )

    self.threat_label.configure(
            text="Threat Level: LOW",
            text_color="green"
        )

    self.warning_label.configure(
            text="SYSTEM SECURE",
            text_color="green"
        )

    elf.encrypted_count.configure(
            text="Simulated Encrypted: 0"
        )

    self.log("Recovery completed")
    self.log("All simulated files restored")

    messagebox.showinfo(
            "Recovery",
            "Simulation reset successfully."
        )