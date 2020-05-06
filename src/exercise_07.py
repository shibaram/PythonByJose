import random

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(range(22), 5))
print(f"lottery_numbers= {lottery_numbers}")
print()
# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}}, #3,5
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}}, #5
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}}, #14,15
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}#3,5,19
]
players_winning_list = []

for player in players:
    players_and_win_counts = {}
    win_tickets_set = lottery_numbers.intersection(player["numbers"])
    current_player_name = player["name"]
    print(f"{current_player_name} has winning tickets as : {str(win_tickets_set)}")
    players_and_win_counts["name"] = current_player_name
    players_and_win_counts["wincounts"] = len(win_tickets_set)
    players_winning_list.append(players_and_win_counts)
print()
winner_name = ""
winner_ticket_count = 0

for p_won in players_winning_list:
    nameofplayer = p_won["name"]
    tickets_won = p_won["wincounts"]
    #winner_name = nameofplayer
    #winner_ticket_count = tickets_won
    print(f"{nameofplayer} has won {tickets_won} tickets")
    if winner_ticket_count < tickets_won:
        winner_ticket_count = tickets_won
        winner_name = nameofplayer

print()
# Then, print out a line such as "Jen won 1000.".
# The winnings are calculated with the formula:
# 100 ** len(numbers_matched)
winning_price = 100 * winner_ticket_count
print(f"{winner_name} has won {winning_price}.")