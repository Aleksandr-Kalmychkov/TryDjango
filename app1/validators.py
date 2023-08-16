from django.core.exceptions import ValidationError
def validate_file_size(value):
    filesize= value.size
    
    if filesize > 20971520:
        raise ValidationError("Размер файла превышает допустимый. Загрузите файл размером не более 20Мб")
    else:
        return value