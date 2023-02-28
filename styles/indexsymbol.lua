rawset(_G, "indexsymbol", {})

do
  local symboltable = {}
  local currentorder = 0

  indexsymbol.run = function(symbol)
    if symboltable[symbol] == nil then
      currentorder = currentorder + 1
      symboltable[symbol] = currentorder
    end

    local order = string.format("%03d", symboltable[symbol])
    tex.sprint("\\index{" .. order .. "@" .. symbol .. "}")
  end
end
