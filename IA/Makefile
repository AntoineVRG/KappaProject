##
## EPITECH PROJECT, 2021
## Makefile
## File description:
## Makefile
##

SRC	=	main.py		\

NAME	=	ia

all :		$(NAME)

$(NAME):
	cp $(SRC) $(NAME)
	chmod +755 $(NAME)

clean:
	rm -f $(NAME)
	rm -rf __pycache__

re : clean all

.PHONY: clean re