#!/bin/bash

python3 -m grpc_tools.protoc -I ./ --python_out=./python/hackermatch/grpc/stubs/ --grpc_python_out=./python/hackermatch/grpc/stubs/ *.proto
protol --create-package --in-place --python-out ./python/hackermatch/grpc/stubs protoc --proto-path=./ *.proto
