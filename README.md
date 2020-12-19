# gimpfu-iexec

# Distributed gimpfu execution

<p align="center">
<img src="https://user-images.githubusercontent.com/6378201/101988273-dfa8a880-3c98-11eb-8a28-c26f113d4fbe.png" alt="before"/>
</p>
<p align="center">
<img src="https://user-images.githubusercontent.com/6378201/101988277-e2a39900-3c98-11eb-93f6-0eca2411a17f.png" alt="after"/>
</p>

This application leverages gimp's batch mode in order to apply a set of effects on multiple images. The computational processing can be negociated with iExec workers.

### Prerequisites
Please refer to the iExec [documentation](https://docs.iex.ec/for-developers/your-first-app)

### Running locally
>   For more visually appealing results, use higher quality images.

Create your input and output folders, then pass them as a parameters in your docker run :

```
docker build . --tag gimpfu-iexec
docker run --rm -v /home/user/iexec_in:/iexec_in -v /home/user/iexec_out:/iexec_out -e IEXEC_IN=/iexec_in -e IEXEC_OUT=/iexec_out gimpfu-iexec
```

The result can be found in $IEXEC_OUT

### Running with iExec
>   For distributed execution testing purposes, use low quality images.

This section assumes you have: 
 - Created and filled your wallet with ETH + RLC
 - Configured your API keys and chain configuration files (chain.json)
 - Deployed your docker image to Docker Hub
 - Deployed your application to iExec

Please refer to the [quickstart guide](https://docs.iex.ec/for-developers/quick-start-for-developers) to perform the necessary steps.

Executing in the goerli testnet :
```
iexec app run --watch --input-files <image url 1>,<image url 2> --chain goerli --workerpool <address>
```
Additional running options can be found [here](https://github.com/iExecBlockchainComputing/iexec-sdk).

You'll find below a minimalistic version of the configuration files :

##### chain.json 
```
{
  "default": "goerli",
  "chains": {
    "goerli": {
      "id": "5"
    }
  },
  "providers": {
    "infura": {
      "projectId": "<infura_projet_id>",
      "projectSecret": "<infura_projet_secret>"
    },
    "quorum": 1
  }
}
```
#####  iexec.json
```
{
  "app": {
    "owner": "<your_ethereum_wallet_address>",
    "name": "gimpfu-iexec",
    "type": "DOCKER",
    "multiaddr": "registry.hub.docker.com/<docker_username>/<docker_image_name>:<docker_image_version>",
    "checksum": "<docker_image_checksum>",
    "mrenclave": ""
  }
}
```
##### Fetching results

```
iexec task show <task_id> --download my-app-result --chain goerli && unzip my-app-result.zip -d my-app-result
```
You can also download your results using the [iExec explorer](https://v5.explorer.iex.ec/goerli/task/0x018e5c996d32792681a946a4705665cef3273079062083bb39ba739c1f261f30).


---
### The tunnel
The following video was made using this gimpfu script in order to process more than 80 files with 4k resolution:  https://vimeo.com/490181629

