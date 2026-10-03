import pytest
from core.translator import translate
from core.parser import parse

@pytest.mark.parametrize("target",["python","c","cpp","java","csharp","javascript","visual-basic","sql","r","rust"])
def test_print_supported_everywhere(target):
    assert translate("print hello world",target).strip()

def test_variable_python():
    assert "speed = 100" in translate("create a variable called speed equal to 100","python")

def test_repeat_cpp():
    assert "i<3" in translate("repeat 3 times print hello","cpp")

def test_sql_table():
    assert "CREATE TABLE users" in translate("create table users with id integer, name varchar(100)","sql")

def test_multiple_commands():
    result=translate("set x equal to 5; increase x by 2; print done","python")
    assert "x = x + 2" in result

def test_extra_commands():
    result=translate("ask name with prompt Name:; wait 1 second; clear","python")
    assert "input" in result and "time.sleep" in result and "\\033[2J" in result

def test_if_alias():
    assert ">= 18" in translate("if age is at least 18 then print adult","python")

def test_while():
    assert "while score < 10" in translate("while score is less than 10 then print waiting","python")

def test_unknown_command():
    with pytest.raises(Exception):
        parse("do something mysterious")
