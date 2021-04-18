#!/usr/bin/env bash
docker run -it -v $PWD:/usr/src/ openjdk:7 bash -c "cd /usr/src/Cypher;export CLASSPATH=../antlr.jar;java org.antlr.v4.Tool -Dlanguage=Python3  -visitor Cypher.g4"
docker run -it -v $PWD:/usr/src/ openjdk:7 bash -c "cd /usr/src/Gremlin;export CLASSPATH=../antlr.jar;java org.antlr.v4.Tool -Dlanguage=Python3  -visitor Gremlin.g4"
python3 Cypher/test.py
# python3 Cypher/test.py