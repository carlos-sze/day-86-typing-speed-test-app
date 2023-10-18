import tkinter as tk
import time


class TypingSpeedTestApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Typing Speed Test")

        self.sample_text = """
        Python is a high-level, interpreted programming language. It was created by Guido van Rossum and first released in 1991. Python's design philosophy emphasizes code readability with its use of significant indentation. It provides constructs that enable clear programming on both small and large scales.

        Python features a dynamic type system and automatic memory management. It supports multiple programming paradigms, including object-oriented, imperative, functional, and procedural, and has a large and comprehensive standard library.

        The language's core philosophy is summarized in the document "The Zen of Python" (PEP 20), which includes aphorisms such as "Beautiful is better than ugly", "Explicit is better than implicit", and "Readability counts".

        Python is often described as a "batteries included" language due to its comprehensive standard library. It comes with modules and packages for tasks such as web development, GUI programming, scientific computing, and data analysis.

        In recent years, Python has become one of the most popular programming languages, primarily due to its simplicity and versatility. It is widely used in various domains, including web development, data analysis, artificial intelligence, and automation.
        """

        self.words = self.sample_text.split()
        self.current_word = ""
        self.total_words = 0
        self.correct_words = 0
        self.start_time = 0
        self.time_limit = 60  # 1 minute

        self.label_sample_text = tk.Label(self, text=self.sample_text, font=("Helvetica", 12), wraplength=500,
                                          justify="left")
        self.label_sample_text.pack(pady=10)

        self.label_instructions = tk.Label(self,
                                           text="Instructions: Click Start to begin. Type the word that appears, then press Enter. Then type the next word that appears.",
                                           font=("Helvetica", 12), wraplength=500, justify="left")
        self.label_instructions.pack(pady=10)

        self.label_current_word = tk.Label(self, text=self.current_word, font=("Helvetica", 14))
        self.label_current_word.pack(pady=10)

        self.entry_typing = tk.Entry(self, font=("Helvetica", 14))
        self.entry_typing.pack(pady=10)
        self.entry_typing.bind('<Return>', self.check_typing)

        self.label_result = tk.Label(self, text="", font=("Helvetica", 14))
        self.label_result.pack(pady=20)

        self.button_start = tk.Button(self, text="Start", command=self.start_typing)
        self.button_start.pack(pady=10)

    def start_typing(self):
        self.total_words = 0
        self.correct_words = 0
        self.start_time = time.time()
        self.label_result.config(text="")
        self.show_next_word()
        self.entry_typing.config(state="normal")
        self.entry_typing.delete(0, tk.END)
        self.entry_typing.focus()
        self.button_start.config(state="disabled")
        self.countdown_timer(self.time_limit)

    def countdown_timer(self, remaining_time):
        if remaining_time >= 0:
            self.label_result.config(text=f"Time remaining: {remaining_time} seconds")
            self.after(1000, self.countdown_timer, remaining_time - 1)
        else:
            self.entry_typing.config(state="disabled")
            elapsed_time = time.time() - self.start_time
            words_per_minute = int(self.correct_words / elapsed_time * 60)
            self.label_result.config(text=f"Words per minute: {words_per_minute}")
            self.button_start.config(state="normal")

    def show_next_word(self):
        if self.total_words < len(self.words):
            self.current_word = self.words[self.total_words]
            self.label_current_word.config(text=self.current_word)
            self.total_words += 1
        else:
            self.current_word = ""
            self.label_current_word.config(text="")

    def check_typing(self, event):
        typed_word = self.entry_typing.get().strip()
        if typed_word == self.current_word:
            self.correct_words += 1
        self.show_next_word()
        self.entry_typing.delete(0, tk.END)
        self.entry_typing.focus()


if __name__ == "__main__":
    app = TypingSpeedTestApp()
    app.mainloop()