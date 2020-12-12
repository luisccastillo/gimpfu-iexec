# gimpfu-iexec

# Gimpfu on iExec

<p align="center">
<img src="https://user-images.githubusercontent.com/6378201/101988273-dfa8a880-3c98-11eb-8a28-c26f113d4fbe.png" alt="before"/>
</p>
<p align="center">
<img src="https://user-images.githubusercontent.com/6378201/101988277-e2a39900-3c98-11eb-93f6-0eca2411a17f.png" alt="after"/>
</p>

This POC application leverages gimp's batch mode in order to apply a cartoonish effect(which goes well with snowy colors) on multiple images. Since execution tmies may take too long to process, the work can be negociated with iExec workers.

## Links 
* Application https://explorer.iex.ec/goerli/app/0xbE446c5BdDAF84Df341c8A6a3408Cc106928c70a
* Docker image https://hub.docker.com/r/lcarloscastillo/gimpfu-iexec/tags?page=1&ordering=last_updated

To test locally use:
docker run --rm -v /home/iexec/iexec-projets/gimpfu-iexec/iexec_in:/iexec_in -v /home/iexec/iexec-projets/gimpfu-iexec/iexec_out:/iexec_out -e IEXEC_IN=/iexec_in -e IEXEC_OUT=/iexec_out gimpfu-iexec

make sure to create both the input and output folders

### The tunnel
The following video was made using gimpfu in batch mode in order to process more than 80 files (of 10 MB each)
* Le tunnel https://vimeo.com/490181629
