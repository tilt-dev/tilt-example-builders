# tilt-example-builders

A collection of examples of how to use Tilt with different image builders.

## Contents

### kubectl build

Drop-in replacement for `docker build` that moves builds off your laptop.

`kubectl build` deploys Docker BuildKit to a Kubernetes pod and builds the image in-cluster.

Example code: [./kubectl_build](./kubectl_build)
