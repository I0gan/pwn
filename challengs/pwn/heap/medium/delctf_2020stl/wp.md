连续施放两次可以构造teach bin的环,先泄漏heap,再通过teach attack打入tecache管理的heap,修改里面的内容,实现unsoretd bin泄漏libc地址,然后再次利用tecache打入malloc_hook处realloc调整参数.实现get shell
