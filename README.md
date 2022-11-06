=== Python reqover 

1. Run tests and observe folder reqover-results
2. Download swagger.json file https://petstore.swagger.io/v2/swagger.json
3. Run command to generate coverage report

```commandline
npx reqover generate -f swagger.json -d reqover-results --html
```

Folder .reqover should appear 

```commandline
npx reqover serve
```

4. Open browser at http://localhost:3000