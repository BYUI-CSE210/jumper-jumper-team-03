class Parachute:
    """The display of the jumper.
    
    The responsibility of the Parachute is to show in the terminal window how many chances the player has left by showing lines of the parachute left.
    
    Attributes:
        parachute(dict[str]): a dictonary of strings.
        parachute_level: current level of parachute [4-0]
        """

    def __init__(self):
        """Constructs a new Parachute
        
        Args: 
            self(Parachute): An instance of a Parachute.
            """
        self._parachute_level = 4
        self._parachute = {
            4:
            """
             ___ 
            /___\\
            \   / 
             \ / 
              0  
             /|\ 
             / \ 
            
            ^^^^^^^
            """,
            3:
            """
            /___\\
            \   / 
             \ / 
              0  
             /|\ 
             / \ 
            
            ^^^^^^^
            """,
            2:
            """
            \   /
             \ / 
              0  
             /|\ 
             / \ 
            
            ^^^^^^^
            """,
            1:
            """
             \ / 
              0  
             /|\ 
             / \ 
            
            ^^^^^^^
            """,
            0:
            """
              X  
             /|\ 
             / \ 
            
            ^^^^^^^
            """
            }

    def get_parachute(self):
        """Gets the current parachute.
        
        Returns: 
            index_number: The current index of the parachute."""
        return self._parachute[self._parachute_level]

    def parachute_remaining(self, parachute):
        """Retrieves how much of the parachute is left.
        
        Args: 
            self: an instance of a parachute
            parachute: the current amount of parachute left."""
        self._parachute_level = parachute