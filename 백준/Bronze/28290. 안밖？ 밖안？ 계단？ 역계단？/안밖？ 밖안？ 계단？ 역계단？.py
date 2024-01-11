import sys

target = sys.stdin.readline().rstrip()

in_out = ["fdsajkl;", "jkl;fdsa"]
out_in = ["asdf;lkj", ";lkjasdf"]
stair = ["asdfjkl;"]
reverse_stair = [";lkjfdsa"]

if target in in_out:
    print("in-out")
elif target in out_in:
    print("out-in")
elif target in stair:
    print("stairs")
elif target in reverse_stair:
    print("reverse")
else:
    print("molu")
