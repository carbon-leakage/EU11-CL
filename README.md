# EU11-CL

## 11 Node European Power System Model with Carbon Pricing


The model is based on the python package "PyPSA" (Python for Power System Analysis): https://pypsa.org/

It can be imported at python runtime via:

```
import pypsa

network = pypsa.Network(csv_folder_name='./model/network/')
```

For more details see "**./model/run.py**"


The power flow tracing is based on the python package "netallocation": https://github.com/FRESNA/netallocation

It is recommended to set up a separate environment (e.g. conda) when using the netallocation package.
