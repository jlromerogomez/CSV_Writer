class CSV_Writer():
   def __init__(self, num_rows, num_cols):
      self._num_rows = num_rows
      self._num_cols = num_cols
      self._table_csv = []
      for iFiles in range(num_rows):
         self._table_csv.append( ['']*num_cols )

   def __str__(self):
      interna = 0
      str_ret = ''
      for ii in self._table_csv:
         interna = interna + 1
         str_ret = str_ret + "LISTA FINAL [{}] {}\n".format(interna, ii)
      return str_ret

   def write_into(self, num_row, num_col, str_in):
      ret = True
      if num_row > 0 and num_row <= self._num_rows  and num_col > 0 and num_col <= self._num_cols:
         row_modifiy = self._table_csv[num_row-1]
         row_modifiy[num_col-1] = str_in
      else:
         ret = False
      return ret

   def dump_to_file(self, output_file):
      with open(output_file, mode='w', newline='') as csv_file:
         csv_writer = csv.writer(csv_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
         for line_csv in self._table_csv:
            print(line_csv)
            csv_writer.writerow(line_csv)
