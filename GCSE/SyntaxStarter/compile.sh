#!/bin/bash

pandoc -t revealjs SyntaxStarter.md -o SyntaxStarter.html -sV revealjs-url=https://revealjs.com

pandoc -t beamer SyntaxStarter.md -o SyntaxStarter.pdf
