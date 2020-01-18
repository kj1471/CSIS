#!/bin/bash

pandoc -t revealjs slides.md -o index.html -sV revealjs-url=https://revealjs.com

pandoc -t beamer slides.md -o presentation.pdf
