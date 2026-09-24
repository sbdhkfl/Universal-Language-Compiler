import pytest
from core.translator import translate
from core.parser import parse

@pytest.mark.parametrize("target",["python","c","cpp","java","csharp","javascript","visual-basic","sql","r","rust"])
def test_print_supported_everywhere(target): assert translate("print hello world",target).strip()

def test_variable_python(): assert "speed = 100" in translate("create a variable called speed equal to 100","python")
def test_repeat_cpp(): assert "i<3" in translate("repeat 3 times print hello","cpp")
def test_sql_table(): assert "CREATE TABLE users" in translate("create table users with id integer, name varchar(100)","sql")
def test_unknown_command():
    with pytest.raises(Exception): parse("do something mysterious")
