
class AlbumParameterValidator():

    
    def __init__(self, album_title, release_year):
        self.album_title = album_title
        self.release_year = release_year

    def _release_year_is_int(self):
        try:
            return self.release_year.isdigit()
        except:
            return False

    def _is_title_none_or_blank(self):
        return self.album_title == None or self.album_title == ""
    
    def _is_release_year_none_or_blank(self):
        return self.release_year == None or self.release_year == ""

    def _is_title_under_255(self):
        return len(self.album_title) <= 255
    
    def _is_release_year_correct_length(self):
        return len(str(self.release_year)) <= 4

    def _is_valid(self):
        if self._is_title_none_or_blank() == True or self._is_release_year_none_or_blank() == True:
            return False
        else:
            return self._is_title_under_255() and self._is_release_year_correct_length()

    def generate_errors(self):
        errors = []
        if self._is_title_none_or_blank() == True:
            errors.append("Album title cannot be blank")
        if self._is_release_year_none_or_blank() == True:
            errors.append("Release year cannot be blank")
        if self._is_release_year_correct_length() == False:
            errors.append("Release year needs to be less than or equal to 4 digits")
        if self._release_year_is_int() == False:
            errors.append("Release year must be an integer")
        if self._is_title_under_255() == False:
            errors.append("Title must be under 255 characters")
        return errors
        