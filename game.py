from rich.console import Console
from engine import Question, Match


console = Console()


questions = [
    Question(
        "پایتخت ژاپن کدام است؟",
        ["توکیو", "کیوتو", "اوساکا", "سئول"],
        "A"
    ),
    Question(
        "خروجی len('سلام') چیست؟",
        ["3", "4", "5", "خطا"],
        "B"
    ),
    Question(
        "بزرگ‌ترین سیاره‌ی منظومه‌ی شمسی؟",
        ["زمین", "زحل", "مشتری", "نپتون"],
        "C"
    ),
    Question(
        "نماد شیمیایی طلا چیست؟",
        ["Ag", "Au", "Fe", "Gd"],
        "B"
    ),
    Question(
        "شاهنامه اثر کیست؟",
        ["حافظ", "سعدی", "فردوسی", "مولوی"],
        "C"
    ),
]


def show_menu():
    console.print("\n⚔  Quiz Battle  ⚔", style="bold cyan")
    console.print("۱) بازی جدید", style="bold green")
    console.print("۲) خروج", style="bold red")


def play():
    player1 = input("نام بازیکن اول: ").strip()
    player2 = input("نام بازیکن دوم: ").strip()

    try:
        match = Match(player1, player2, questions)
    except ValueError as e:
        console.print(f"خطا: {e}", style="bold red")
        return

    while not match.is_over():
        question = match.start_round()

        console.print(
            f"\nسؤال {match.round} از {len(questions)}:",
            style="bold cyan"
        )

        console.print(question.text, style="bold")

        for letter, option in zip("ABCD", question.options):
            console.print(f"  {letter}) {option}", style="bold")

        answer1 = input(f"{player1}، جواب تو (A-D): ").strip().upper()
        match.submit(player1, answer1, 0)

        answer2 = input(f"{player2}، جواب تو (A-D): ").strip().upper()
        match.submit(player2, answer2, 0)

        match.resolve_round()

        console.print("\nامتیاز فعلی:", style="bold yellow")
        console.print(
            f"  {player1}: {match.scores[player1]}",
            style="bold green"
        )
        console.print(
            f"  {player2}: {match.scores[player2]}",
            style="bold green"
        )

    winner = match.winner()

    console.print("\nبازی تمام شد!", style="bold yellow")

    if winner is None:
        console.print("نتیجه: مساوی!", style="bold cyan")
    else:
        console.print(
            f"برنده: {winner}",
            style="bold green"
        )

    console.print(
        f"{player1}: {match.scores[player1]}",
        style="bold"
    )
    console.print(
        f"{player2}: {match.scores[player2]}",
        style="bold"
    )


while True:
    show_menu()

    choice = input("انتخاب تو (۱ یا ۲): ").strip()

    if choice in ("1", "۱"):
        play()

    elif choice in ("2", "۲"):
        console.print("خداحافظ!", style="bold cyan")
        break

    else:
        console.print(
            "فقط ۱ یا ۲ را وارد کن.",
            style="bold yellow"
        )
