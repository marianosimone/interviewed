class SpreadsheetColRowIndexer:
    COLS = dict([(c, i+1) for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")])

    @staticmethod
    def col_index_from_name(name):
        """
        Given the name of a column in a spreadsheet, return its index (1-based)

        >>> SpreadsheetColRowIndexer.col_index_from_name('A')
        1
        >>> SpreadsheetColRowIndexer.col_index_from_name('B')
        2
        >>> SpreadsheetColRowIndexer.col_index_from_name('AA')
        27
        >>> SpreadsheetColRowIndexer.col_index_from_name('AMJ')
        1024
        """
        base = len(SpreadsheetColRowIndexer.COLS)
        rv = 0
        for i in xrange(0, len(name)):
            c = name[-i-1]
            rv += (base**i)*SpreadsheetColRowIndexer.COLS[c]
        return rv
