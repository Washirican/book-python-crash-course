# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-04
# --------------------------------------------------------------------------- #


def show_messages(unsent_messages, sent_messages):
    """Send messages."""
    while unsent_messages:
        current_message = unsent_messages.pop()
        print(f'\nSending message: {current_message.title()}')
        sent_messages.append(current_message)


unsent_messages = ['i love python', 'the future is female', 'carpe diem']
sent_messages = []
show_messages(unsent_messages[:], sent_messages)

print()
print(unsent_messages)
print(sent_messages)


