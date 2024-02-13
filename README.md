# deps-shared-mod-a
Dependency Management Demo: Reusable Module A (used by SWC1 and possibly other SWCs)

## Preparation
You can build this package like this:
```sh
conan create . --version 1.3.0
```

If you haven't configured conan yet, point it to the right repository by running "conan remote add". Here's an example for a conan repo in artifactory:
```sh
conan remote add artifactory http://$host:$port/artifactory/api/conan/$reponame
```

Afterwards, you can upload the package via 
```sh
conan upload shared_module_a -r artifactory
```
