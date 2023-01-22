# gRPC Protobuf Definitions

## Generating Stubs

### Python

You will need to first install the base package with extras to get the needed tools: `python3 -m pip install ".[generate_stubs]"`. 

To generate Python code from these protobuf definitions, run the following command: `python3 -m grpc_tools.protoc -I ./ --python_out=./python/hackermatch/grpc/stubs/ --grpc_python_out=./python/hackermatch/grpc/stubs/ *.proto`.

Next, you'll need to run a special tool that fixes buggy protoc imports: `protol --create-package --in-place --python-out ./python/hackermatch/grpc/stubs protoc --proto-path=./ *.proto`

Finally, run `python3 -m pip install .` to install the updated stubs to your Python environment.

- or -

You can simply run `./regenerate_stubs.sh`
