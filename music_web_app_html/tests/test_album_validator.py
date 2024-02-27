from lib.album_parameter_validator import *

"""
test is valid
"""
def test_is_valid():
    validator = AlbumParameterValidator("My Title", "1990")
    assert validator._is_valid() == True

"""
test passes in None value for Title
"""
def test_has_none_values_name():
    validator_1 = AlbumParameterValidator(None, "1990")
    validator_2 = AlbumParameterValidator("", "1990")
    assert validator_1._is_valid() == False
    assert validator_2._is_valid() == False

"""
test passes in None value for release year
"""
def test_is_missing_release_year():
    validator = AlbumParameterValidator("My Title", None)
    assert validator._is_valid() == False
    assert validator.generate_errors() == ['Release year cannot be blank','Release year must be an integer']

"""
release year is not an integer
"""

def test_release_year_not_int():
    validator_1 = AlbumParameterValidator("My Title", "string")
    validator_2 = AlbumParameterValidator("My Title", "")    
    assert validator_1._is_valid() == False
    assert validator_2._is_valid() == False
    assert validator_1.generate_errors() == ["Release year needs to be less than or equal to 4 digits", "Release year must be an integer"]

"""
title is too long
"""
def test_very_long_title():
    validator = AlbumParameterValidator("Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a", "2020")
    print(len(validator.album_title))
    print(validator._is_valid())
    print(validator._is_title_under_255())
    assert validator._is_valid() == False
    assert validator.generate_errors() == ["Title must be under 255 characters"]

"""
test if integer is too long fails and returns error message
"""
def test_is_valid():
    validator = AlbumParameterValidator("My Title", "1990289")
    assert validator._is_valid() == False
    assert validator.generate_errors() == ["Release year needs to be less than or equal to 4 digits"]

