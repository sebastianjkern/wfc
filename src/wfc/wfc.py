# %%
tiles = [[set([1, 2, 3, 4, 5, 6, 7])] * 5] * 5
tiles
# %% The ruleset gives each relative position a set of possible states
rules = {
    (1, 1): set([1, 2, 3, 4, 5, 6]),
    (-1, 0): set([1, 2, 3])
}
rules

# %% Function for collapsing a single cell, 
# subsequent cells are NOT collapsed
def _collapse(x, y, ruleset, tiles):
    temp = tiles.copy()
    changeset = []

    for dx, dy in ruleset.keys():
        temp[x + dx][y + dy] = tiles[x + dx][y + dy] & rules[(dx, dy)]
        changeset.append((x + dx, y + dy))

    return temp, changeset

# %%

def _collapse(x, y, ruleset, tiles):
    temp = tiles.copy()
    changeset = []

    for dx, dy in ruleset.keys():
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(tiles) and 0 <= ny < len(tiles[0]):  # Check if the index is within bounds
            temp[nx][ny] = tiles[nx][ny] & ruleset[(dx, dy)]
            changeset.append((nx, ny))

    return temp, changeset

def recursive_collapse(x, y, ruleset, tiles):
    updated_tiles, changeset = _collapse(x, y, ruleset, tiles)

    for cx, cy in changeset:
        updated_tiles = recursive_collapse(cx, cy, ruleset, updated_tiles)

    return updated_tiles

# %%

recursive_collapse(1, 1, rules, tiles)