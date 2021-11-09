# tilt-example-builders

[![Build Status](https://circleci.com/gh/tilt-dev/tilt-example-builders/tree/main.svg?style=shield)](https://circleci.com/gh/tilt-dev/tilt-example-builders)

A collection of examples of how to use Tilt with different image builders.

## Contents

### kubectl build

Drop-in replacement for `docker build` that moves builds off your laptop.

`kubectl build` deploys Docker BuildKit to a Kubernetes pod and builds the image in-cluster.

Install kubectl build: [homepage](https://github.com/vmware-tanzu/buildkit-cli-for-kubectl#getting-started)

Example Tiltfile: [./kubectl_build](./kubectl_build/Tiltfile)

### ko

Turn-key Go apps without any fuss.

Runs `go build` locally and packs it into an image.

`ko` works best when your Go app is a simple static binary, and doesn't have any 
dependencies on the OS environment (e.g., loading dynamic C libraries.)

Install ko: [homepage](https://github.com/google/ko#install)

Example Tiltfile: [./ko](./ko/Tiltfile)

### pack

Stackable image builders to add whatever you need to an image.

Buildpacks give you better control over what ends up in the final container image.
It's easier to keep out the junk you don't want (like buildtools), and
keep the good stuff you do want (like hot-reloading).

Install pack: [homepage](https://buildpacks.io/docs/tools/pack/)

Example Tiltfile: [./pack](./pack/Tiltfile)
