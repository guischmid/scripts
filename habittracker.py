import json
import os
from datetime import datetime, timedelta

# Datei, in der die Gewohnheiten gespeichert werden
FILE_NAME = 'habit_data.json'

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return {}

def save_data(data):
    with open(FILE_NAME, 'w') as file:
        json.dump(data, file, indent=4)

def add_habit(data, habit_name):
    if habit_name in data:
        print(f"Die Gewohnheit '{habit_name}' existiert bereits.")
    else:
        data[habit_name] = {'dates': [], 'streak': 0}
        save_data(data)
        print(f"Gewohnheit '{habit_name}' wurde hinzugefügt.")

def mark_habit_done(data, habit_name):
    today = datetime.now().strftime('%Y-%m-%d')
    if habit_name in data:
        if today not in data[habit_name]['dates']:
            data[habit_name]['dates'].append(today)
            calculate_streak(data, habit_name)
            save_data(data)
            print(f"Gewohnheit '{habit_name}' wurde für heute erledigt.")
        else:
            print(f"Die Gewohnheit '{habit_name}' wurde bereits heute markiert.")
    else:
        print(f"Die Gewohnheit '{habit_name}' existiert nicht.")

def calculate_streak(data, habit_name):
    dates = [datetime.strptime(date, '%Y-%m-%d') for date in data[habit_name]['dates']]
    dates.sort()
    
    streak = 0
    for i in range(len(dates) - 1):
        if (dates[i + 1] - dates[i]).days == 1:
            streak += 1
        else:
            streak = 0
    
    data[habit_name]['streak'] = streak + 1 if dates else 0

def show_stats(data, habit_name):
    if habit_name in data:
        total_days = len(data[habit_name]['dates'])
        current_streak = data[habit_name]['streak']
        print(f"Statistiken für '{habit_name}':")
        print(f"- Insgesamt erledigte Tage: {total_days}")
        print(f"- Aktuelle Streak: {current_streak} Tage")
    else:
        print(f"Die Gewohnheit '{habit_name}' existiert nicht.")

def main():
    data = load_data()
    
    while True:
        print("\nMenu:")
        print("1. Neue Gewohnheit hinzufügen")
        print("2. Gewohnheit als erledigt markieren")
        print("3. Statistiken anzeigen")
        print("4. Beenden")
        
        choice = input("\nWähle eine Option: ")
        
        if choice == '1':
            habit_name = input("Name der Gewohnheit: ")
            add_habit(data, habit_name)
        elif choice == '2':
            habit_name = input("Name der Gewohnheit: ")
            mark_habit_done(data, habit_name)
        elif choice == '3':
            habit_name = input("Name der Gewohnheit: ")
            show_stats(data, habit_name)
        elif choice == '4':
            print("Tschüss!")
            break
        else:
            print("Ungültige Wahl, bitte versuche es erneut.")

if __name__ == "__main__":
    main()