# tilt-example-builders

[![Build Status](https://circleci.com/gh/tilt-dev/tilt-example-builders/tree/main.svg?style=shield)](https://circleci.com/gh/tilt-dev/tilt-example-builders)

A collection of examples of how to use Tilt with different image builders.

## Contents

### kubectl build

Drop-in replacement for `docker build` that moves builds off your laptop.

`kubectl build` deploys Docker BuildKit to a Kubernetes pod and builds the image in-cluster.

Install kubectl build: [homepage](https://github.com/vmware-tanzu/buildkit-cli-for-kubectl#getting-started)

Example Tiltfile: [./kubectl_build](./kubectl_build/Tiltfile)
