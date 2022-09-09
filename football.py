import random


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 0:
            self.__age = age
        else:
            raise Exception("age must be positive")


class Player(Human):
    def __init__(self, name, age, role, score):
        super().__init__(name, age)
        self.role = role
        self.score = score
        self.team = None

    @Human.age.setter
    def age(self, age):
        if 15 < age and age < 30:
            self.__age = age
        else:
            raise Exception("age must be between 15 to 30!")

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if 0 < score and score < 101:
            self.__score = score
        else:
            raise Exception("age must be between 0 to 100!")


class Coach(Human):
    def __init__(self, name, age, sallary, start_convation, end_convation):
        super().__init__(name, age)
        self.sallary = sallary
        self.start_convation = start_convation
        self.end_convation = end_convation

    @Human.age.setter
    def age(self, age):
        if age >= 30 and age <= 60:
            self.__age = age
        else:
            raise Exception("age must be between 30 to 60!")

    @property
    def team(self):
        return self._team

    @team.setter
    def team(self, chosen_team):
        self._team = chosen_team


class Team:
    # coaches=[]

    def __init__(self, name, balance, grade):
        self.player_list = []
        self.name = name
        self.grade = grade
        self.balance = balance

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, grade):
        if grade < 0:
            raise Exception("grade must be positive!")
        self.__grade = grade

    def check_player_number(self):
        if len(self.player_list) == 11:
            return True
        return False

    def add_player(self, players_info):
        for info in players_info:
            if not self.check_player_number():
                new_player = Player(info[0], info[1], info[2], info[3])
                self.player_list.append(new_player)
                new_player.team = self

    def add_coach(self, coach):
        if coach not in Team.coaches:
            self.coach = coach
            Team.coaches.append(coach)
        else:
            print("This coach is reserved")

    def transfer_player(self, player):
        player_cost = player.score*1000
        if self.check_player_number and self.balance >= player_cost:
            self.player_list.append(player)
            self.balance -= player_cost
            player.team.balance += player_cost
            player.team = self
        else:
            print("This transfer is imposible!")

    def __lt__(self, other):
        if self.grade == other.grade:
            return self.name < other.name
        return self.grade < other.grade

    def __repr__(self):
        return f"{self.name} - {self.grade}"


class Ligue:

    def __init__(self, name, teams):
        self.name = name
        self.teams = teams

    @property
    def teams(self):
        return self.__teams

    @teams.setter
    def teams(self, team_list):
        if len(team_list) == 5:
            for team in team_list:
                if not team.check_player_number:
                    raise Exception("This Ligue cant be cerated")
            self.teams = team_list
        else:
            raise Exception("This Ligue cant be cerated")

    def choose_champions(self):
        for i in range(4):
            lst = random.sample(self.teams, k=2)
            Ligue.assign_score(lst[0], lst[1])

    @staticmethod
    def assign_score(team1, team2):
        score = random.sample([[1, 1], [3, 0], [0, 3]], k=1)
        team1.grade += score[0]
        team2.grade += score[1]


coach1 = Coach('ali', 40, 200000, '1401/01/01', '1401/05/01')
team1 = Team("perspolis", 1000000, 22)
info = [['p1', 17, 'g1', 20], ['p2', 22, 'g2', 30], ['p3', 17, 'g3', 20]]
team1.add_player(info)
print(team1.player_list)
coach2 = Coach('reza', 40, 2000, '1401/01/01', '1401/05/01')
team2 = Team("esteghlal", 2000000, 22)
# print(team1.player_list[1].team)
# info=[['p1',17,'g1',20],['p2',22,'g2',30],['p3',17,'g3',20]]
team2.transfer_player(team1.player_list[1])
print(team2.player_list)

team5 = Team("ff", 1000000, 22)
team4 = Team("dd", 1000000, 30)
team3 = Team("sephan", 1000000, 40)

lst = [team4, team2, team1, team5, team3]
print(lst)
lst.sort()
print(lst)
