This program allows users easily convert their plot axis in arcsinh scale.
Arcsinh scalse has linear-scalse characteristics around the origin and log-scalse characteristics at larger absolute values, which are varid for all range of real number.
Arcsinh scalse is good for multi-scale analysis. 

call signiture
```
setArcsinh(method, *args, dim=1, **kwargs)
```
This method will execute `return method(*args, **kwargs)` with some arguments defined by `dim` are replaced with arcsinh scale. 

`dim` must be a scaler greator than 0 or iterable containing intecies of `arg` to be replaced.
If `dim` is a scaler, first `dim` arguments will be replaced.

---
### Lisence
This program is published under BSD 3-Clause License by Akito D. Kawamura.

See LISENCE file for more detail.
