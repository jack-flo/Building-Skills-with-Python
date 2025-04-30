# A block of stock is a purchase order for a stock (purchase price, date, no of shares)
# A position is the current ownership of a company represented by all the blocks of the stock
# A portfolio is a collection of positions.

class StockBlock (object):
  """Create a StockBlock"""

  def __init__ (self, purchDate, purchPrice, shares):
    """Create the initial block values"""
    self.date = purchDate
    self.price = purchPrice
    self.numberOfShares = shares

  def __str__ (self):
    """Return a pleasant representation"""
    return (
      f"(Date: {self.date})",
      f"(Price: {self.price:g})",
      f"(Number of Shares: {self.numberOfShares:d})"
    )
  
  def getPurchValue (self):
    """Returns the value at purchase"""
    purchaseValue = self.price * self.numberOfShares
    return purchaseValue
  
  def getSaleValue (self, salePrice):
    """Returns the value of shares when sold at an inputted price"""
    saleValue = salePrice * self.numberOfShares
    return saleValue
  
  def getROI(self, salePrice):
    """Return the ROI as (sale value - purchase value) / purchase value"""
    saleValue = self.getSaleValue(salePrice)
    purchValue = self.getPurchValue()
    return (saleValue - purchValue) / purchValue
  

class Position(object):
  """A position of current ownership of a company represented by a list of blocks"""
  def __init__ (self, name, symbol, * blocks):
    """Accept name, symbol, and collection of StockBlock instances"""
    self.name = name
    self.symbol = symbol
    self.blocks = list(blocks) # add checking later

  def __str__ (self):
    return f"Symbol: {self.symbol}, Total Shares: {self.getTotalShares()}, Total Purchase Price: {self.getTotalPurchasePrice()}"
  
  def getTotalShares(self):
    """Get the total shares in all of the StockBlocks"""
    totalShares = 0
    for block in self.blocks:
      totalShares += block.numberOfShares
    return totalShares
  
  def getTotalPurchasePrice (self):
    """Get the total purchase price for all of the StockBlocks"""
    total = 0
    for block in self.blocks:
      total += block.getPurchValue()
    return total
  
  def getSaleValue (self, salePrice):
    """Returns the value of shares when sold at an inputted price"""
    saleValue = salePrice * self.getTotalShares()
    return saleValue
  
  def getROI(self, salePrice):
    """Return the ROI as (sale value - purchase value) / purchase value"""
    saleValue = self.getSaleValue(salePrice)
    purchValue = self.getTotalPurchasePrice()
    return (saleValue - purchValue) / purchValue


blocksGM = [
StockBlock( purchDate='25-Jan-2001', purchPrice=44.89, shares=17 ),
StockBlock( purchDate='25-Apr-2001', purchPrice=46.12, shares=17 ),
StockBlock( purchDate='25-Jul-2001', purchPrice=52.79, shares=15 ),
StockBlock( purchDate='25-Oct-2001', purchPrice=37.73, shares=21 ),
]
blocksEK = [
StockBlock( purchDate='25-Jan-2001', purchPrice=35.86, shares=22 ),
StockBlock( purchDate='25-Apr-2001', purchPrice=37.66, shares=21 ),
StockBlock( purchDate='25-Jul-2001', purchPrice=38.57, shares=20 ),
StockBlock( purchDate='25-Oct-2001', purchPrice=27.61, shares=28 ),
]

portfolio= [
  Position( "General Motors", "GM", blocksGM ),
  Position( "Eastman Kodak", "EK", blocksEK ),
  Position( "Caterpillar", "CAT",
  [ StockBlock( purchDate='25-Oct-2001',
  purchPrice=42.84, shares=18 ) ] )
]
