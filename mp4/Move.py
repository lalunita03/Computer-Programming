"""
Author: El Hovik
CS 1 Fall 2022
Move class for the Pokemon simulator, supporting PokemonSpecies moves.
This class is provided for students for MP4, though they only use
it when constructing Move objects as follows:
Move(move name, type, accuracy, dmg, buff, buff amt)
Move(str, str, int, int, str, int)

Students may add methods to this class if they are appropriate
when implementing the MiniProject. If they do, they
must submit this file in their CodePost submissions.
Some optional additions could include:

- get_move_label() - returns 'DP', 'Buff', or 'Debuff'
    (get_move_type is another good name, but is confusing with
     the actual move_type string which is a Pokemon type)
- is_dp() - True if DP move, else False for Buff/Debuff
- Use subclasses for a Move called DPMove and BuffMove
    - DPMove would have a dp attribute, no buff attributes,
      and string representation for DP move (see __str__() below)
    - BuffMove would have BUFF_TYPES constant, buff_type attribute,
      buff_amt, and string representation for buffs/debuffs
      (see __str__() below)
"""


class Move:
    # There are three buff types supported in the Pokemon simulator
    BUFF_TYPES = ['Accuracy', 'Attack', 'Defense']

    """
    Represents a Pokemon move object with the following attributes:
    `name` (str) - name of the move (e.g. 'Thunderbolt')
    `type` (str) - type of move (e.g. 'electric')
    `accuracy` (float) - accuracy rating of the move.

    Physical moves (have DP, no buffs):
    `dp` (int) - DP ("damage point") value of the move

    Special Moves (update buffs, no DP):
    `buff` (str) - buff type of move ('Accuracy', 'Attack', or 'Defense')
    `buff_amt` (int) - amount of buff
        + for positive buff,
        0 for none
        - for negative buff
    """
    def __init__(self, move_name, move_type, acc, dp, buff, buff_amt):
        """
        Constructs a Move object with a given `move_name` (str),
        `move_type` (str), `acc` accuracy rate (float between 0.0 and 1.0),
        `dp` damage point count, `buff` buff type (str), and `buff_amt` (int).
        There is some user-friendly argument handling, such as converting a
        non-empty string `dp` or 'buff_amt' like '1' to an int.

        Moves must be either "DP" damage moves without buffs, or "Buff/Debuff"
        moves. A buff move has a positive `buff_amt` to increase a Pokemon's
        stats. A debuff move has a negative `buff_amt` to decrease a Pokemon's
        stats.

        Requirements:
        - `acc` must be between [0.0, 1.0], representing an "accuracy rate"
          of the move.
        - If given a positive `dp` value, the move is considered a DP move and
          buff values are ignored. In "real Pokemon" a move can have both DP
          and buff effects, so students may support this however they want
          (including ignoring buffs for a given DP).
        - Otherwise (`dp` is '', None, or 0) the move is considered a buff move
          with the following requirements:
            - `buff_type` must be a type specified in `BUFF_TYPES`
            - `buff_amt` must be a non-zero number (usually an int)

        If given invalid arguments, raises a ValueError that should
        be handled when calling the constructor.
        """
        # accuracy is required, so convert to float
        acc = float(acc)
        # if given, convert to int to support string int args
        self._validate_args(acc, dp, buff, buff_amt)

        if dp:
            dp = int(dp)
            buff_amt = 0
        elif buff_amt:
            buff_amt = int(buff_amt)
            dp = 0
        self.name = move_name
        self.move_type = move_type
        self.accuracy = acc
        self.dp = dp
        self.buff = buff.capitalize()  # no error on ''
        self.buff_amt = buff_amt

    def __str__(self):
        """
        Returns a string representation of a Move with the move
        name, type, and DP info for DP moves or buff info
        for buff moves (a move is either a DP move or buff move).
        Also specifies whether a move is either a:
        - Buff     (+ buff amount, increasing a Pokemon's stats) or
        - Debuff (- buff amount, decreasing a Pokemon's stats)

        Format for DP moves:
        <move_name>: (Type: <type>, DP: <dp>)
        Example:
        'Thunderbolt: (Type: Electric, DP: 90)'

        Format for Buff/Debuff moves:
        <move_name>: (Type: <type>, Buff/Debuff: <buff_amt> <buff_type>)
        Examples:
        'Growl: (Type: Normal, Debuff: -1 Attack)'
        'Harden: (Type: Normal, Buff: +1 Defense)'
        """
        # Start for all moves, rest is DP or buff info
        result = f'{self.name}: (Type: {self.move_type}, '
        if (self.dp):
            result += f'DP: {self.dp})'
        else:
            buff_amt = self.buff_amt
            # if buff_amt is positive, this is a (good) buff
            buff_type = 'Buff'
            if buff_amt > 0:  # add + for a nice representation
                buff_amt = f'+{buff_amt}'
            else:
                # otherwise buff_amt is negative, this is a (bad) debuff
                buff_type = 'Debuff'
            result += f'{buff_type}: {buff_amt} {self.buff})'
        return result

    # Note to students: You can specify 'private' methods with
    # _ before the method name.
    # _ methods should generally not be used by clients using a class, only
    # to help implement a methods in the class.
    def _validate_args(self, acc, dp, buff_type, buff_amt):
        """
        Validates arguments for constructing a Move object.
        Raises a ValueError for invalid arguments
        in order of requirements:
            - `acc` must be between 0.0 and 1.0
            - If `dp` is falsey ('', None, or 0):
                - `buff_type` must be a type in `BUFF_TYPES`
                - `buff_amt` must be a non-zero number
        """
        if acc < 0.0 or acc > 1.0:
            raise ValueError('Accuracy must be between 0.0 and 1.0')
        # if not a dp move, check requirements for buffs
        # no requirements needed for dp otherwise
        if not dp:
            if not buff_type.capitalize() in self.BUFF_TYPES:
                raise ValueError('Invalid buff given. Supported buffs: ' +
                                 self.BUFF_TYPES.join(','))
            if int(buff_amt) == 0:
                raise ValueError('Buff amount must be non-zero integer.')

    def get_dp(self):
        """
        Returns the Move's dp value ('' or 0 if the move doesn't
        do any damage; that would be a buff/debuff move).

        Returns:
            - (int) DP "damage points" of Move, if a DP move
        """
        return self.dp

    def get_move_name(self):
        """
        Returns the name of this move.

        Returns:
            - (str) name of move.
        """
        return self.name
