# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
ten = 1
one = 10
zero = 1
tenplusone = "ten" + "one"

# %%
print(ten + one)
# %% [markdown]
# (1) Answer is 11. # two integers can be concatenated

# %%
print(ten + 1)
# %% [markdown]
# (2) Answer is 2. # here again, two integers can be concatenated

# %%
print (one - 1 * zero - 0 + 10 ** ten)
# %% [markdown]
# (3) Answer is 19. # multiplications precede additions and subtractions 
# %%
if zero - 1 :
    print('ten')
# %% [markdown]
# (4)  # there is no output here because the condition statement is not complete
 
# %%
print(int(one) * 10 % 1 / int(ten) + 1 ** 10)
# %% 
# (5) Answer is 1.0. # exponentiations precede multiplications, which proceed additions
# %%
print('tenplusone' + tenplusone + 'ten' + one)

# %% # there is a TypeError appeared because integers cannot be concatenated with strings
