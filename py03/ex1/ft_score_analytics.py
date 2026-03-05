import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    if len(sys.argv) < 2:
        print(f"No scores provided. "
              f"Usage: {sys.argv[0]} <score1> <score2> ...")
        sys.exit(1)
    scores = []
    for arg in sys.argv[1:]:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Invalid score: {arg}. Please provide numeric values only.")
            sys.exit()

    print(f"Scores processed: {scores}")
    print(f"Total scores: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores)} ")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")
