class PlayGame:

    # Initialisation method
    def __init__(self, color_o, color_x, color_d, playground):
        self.playground = playground
        self.check_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        self.color_o = color_o
        self.color_x = color_x
        self.color_endc = color_d

    # replace the number with user option and apply the corresponding colors
    def output_playground(self, user, user_option):

        self.playground = self.playground.replace(str(user_option), user)
        return self.playground.replace\
            ("X", self.color_x + "X" + self.color_endc).replace("O", self.color_o + "O" + self.color_endc)

    # check if the user's combination is the winner one
    def check_combination(self, player_combination):
        for sub_array in self.check_array:
            if all([items in player_combination for items in sub_array]):
                return True


