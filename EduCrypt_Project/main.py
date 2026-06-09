import customtkinter as ctk
from tkinter import filedialog
import os
from datetime import datetime

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class EduCryptSimulator:

    def __init__(self, root):
        self.root = root
        self.root.title("EduCrypt - Ransomware Simulator")
        self.root.geometry("1000x650")

        self.files = []
        self.countdown_seconds = 86400

        self.build_ui()
        self.update_timer()

    def start_simulation(self):

        self.show_ransom_note()

        self.status_label.configure(
            text="Attack Status: COMPROMISED"
        )

        self.threat_label.configure(
            text="Threat Level: CRITICAL",
            text_color="red"
        )

        self.warning_label.configure(
            text="WARNING: FILES ARE UNDER ATTACK",
            text_color="red"
        )

        self.log("Attack started")
        self.log("Discovery phase completed")
        self.log("Encryption simulation started")

        self.file_box.delete("1.0", "end")

        self.file_box.insert(
            "end",
            "FILE STATUS\n=====================\n"
        )

        encrypted_count = 0

        for file in self.files:

            filename = os.path.basename(file)

            self.file_box.insert(
                "end",
                f"{filename}  [ENCRYPTED]\n"
            )

            encrypted_count += 1

        self.encrypted_count.configure(
            text=f"Simulated Encrypted: {encrypted_count}"
        )

        self.log(
            f"{encrypted_count} files marked as encrypted"
        )

    def recover(self):

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

        self.log("Recovery completed")


    def log(self, message):
        self.log_box.insert("end", message + "\n")
        self.log_box.see("end")

    def select_folder(self):

        folder = filedialog.askdirectory()

        if not folder:
            return

        self.folder_label.configure(text=folder)

        self.files = []

        for root_dir, dirs, files in os.walk(folder):
            for file in files:
                self.files.append(
                    os.path.join(root_dir, file)
                )

        self.files_count.configure(
            text=f"Files Found: {len(self.files)}"
        )

        self.file_box.delete("1.0", "end")

        self.file_box.insert(
            "end",
            "FILE STATUS\n=====================\n"
        )

        for file in self.files:
            filename = os.path.basename(file)

            self.file_box.insert(
                "end",
                f"{filename}  [NORMAL]\n"
            )

        self.log(f"Folder selected: {folder}")
        self.log(
            f"{len(self.files)} files discovered"
        )

    def build_ui(self):

        title = ctk.CTkLabel(
            self.root,
            text="EDUCRYPT RANSOMWARE SIMULATOR",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=15)

        dashboard = ctk.CTkFrame(self.root)
        dashboard.pack(fill="x", padx=20, pady=5)

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

        top_frame = ctk.CTkFrame(self.root)
        top_frame.pack(fill="x", padx=20, pady=10)

        self.folder_label = ctk.CTkLabel(
            top_frame,
            text="No folder selected"
        )
        self.folder_label.pack(side="left", padx=10)

        self.select_button = ctk.CTkButton(
            top_frame,
            text="Select Folder",
            command=self.select_folder
        )
        self.select_button.pack(side="right", padx=10)

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

        button_frame = ctk.CTkFrame(self.root)
        button_frame.pack(fill="x", padx=20, pady=10)

        self.start_button = ctk.CTkButton(
            button_frame,
            text="Start Simulation",
            command=self.start_simulation
)
        self.start_button.pack(side="left", padx=10)

        self.recover_button = ctk.CTkButton(
            button_frame,
            text="Recover",
            command=self.recover
        )
        self.recover_button.pack(side="left", padx=10)

        self.report_button = ctk.CTkButton(
            button_frame,
            text="Generate Report",
            command=self.generate_report 
        )
        self.report_button.pack(side="left", padx=10)

        bottom_frame = ctk.CTkFrame(self.root)
        bottom_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        self.file_box = ctk.CTkTextbox(
            bottom_frame,
            width=350
        )
        self.file_box.pack(
            side="left",
            fill="both",
            padx=5,
            pady=5
        )

        self.file_box.insert(
            "end",
            "FILE STATUS\n=====================\n"
        )

        self.log_box = ctk.CTkTextbox(
            bottom_frame
        )
        self.log_box.pack(
            side="right",
            fill="both",
            expand=True,
            padx=5,
            pady=5
        )

        self.log_box.insert(
            "end",
            "EVENT LOG\n=====================\n"
        )

    def generate_report(self):

        report_name = (
            f"attack_report_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        )

        with open(report_name, "w") as report:

            report.write("EDUCRYPT INCIDENT REPORT\n")
            report.write("=" * 40 + "\n\n")

            report.write(
                f"Generated: {datetime.now()}\n"
            )

            report.write(
                f"Files Found: {len(self.files)}\n"
            )

            report.write(
                f"Simulated Encrypted: "
                f"{self.encrypted_count.cget('text')}\n"
            )

            report.write(
                f"Threat Level: "
                f"{self.threat_label.cget('text')}\n"
            )

            report.write(
                f"Attack Status: "
                f"{self.status_label.cget('text')}\n"
            )

        self.log(
            f"Report generated: {report_name}"
        )

    def show_ransom_note(self):

        note = ctk.CTkToplevel(self.root)

        note.title("Ransom Note")
        note.geometry("700x450")

        title = ctk.CTkLabel(
            note,
            text="YOUR FILES HAVE BEEN LOCKED",
            font=("Arial", 24, "bold"),
            text_color="red"
        )
        title.pack(pady=20)

        message = ctk.CTkLabel(
            note,
            text=(
                "Victim ID: EDU-2026-001\n\n"
                f"Files Affected: {len(self.files)}\n\n"
                "This is an educational simulation.\n"
                "No files have actually been encrypted."
            ),
            font=("Arial", 16)
        )

        message.pack(pady=20)
        
    def update_timer(self):

        hours = self.countdown_seconds // 3600
        minutes = (
            self.countdown_seconds % 3600
        ) // 60
        seconds = (
            self.countdown_seconds % 60
        )

        self.timer_label.configure(
            text=(
                "DECRYPTION KEY EXPIRES IN\n"
                f"{hours:02}:{minutes:02}:{seconds:02}"
            )
        )

        if self.countdown_seconds > 0:

            self.countdown_seconds -= 1

            self.root.after(
                1000,
                self.update_timer
            )

root = ctk.CTk()
app = EduCryptSimulator(root)
root.mainloop()