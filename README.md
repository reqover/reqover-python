## Python reqover 

[Report example](https://reqover.github.io/reqover-python/)

1. Run recorder

```
docker run -p 3000:3000 -v $PWD:/reqover reqover/reqover-cli record -t https://petstore.swagger.io
```
2. Set your test base host as http://localhost:3000
3. Run tests and observe folder reqover-results
4. Download swagger.json file https://petstore.swagger.io/v2/swagger.json
5. Run command to generate coverage report

```commandline
npx reqover generate -f swagger.json -d reqover-results --html
```

Folder .reqover should appear 

```commandline
npx reqover serve
```

5. Open browser at http://localhost:3000

```
docker run -v $PWD:/reqover \
-v $PWD/data:/tmp/data \
-v $PWD/swagger.json:/tmp/swagger.json \
reqover/reqover-cli generate -f /tmp/swagger.json -d /tmp/data -p /v2 --html                        
```

### License
Reqover python is distributed under the terms of the [Apache license 2.0](http://www.apache.org/licenses/LICENSE-2.0)
