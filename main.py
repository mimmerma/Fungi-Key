import fungiClass as fungiClass

def createDeathCap():
	commonName = 'Death Cap'
	latinName = 'Amanita phalloides'
	family = 'Amanitaceae'
	nativeDistribution = ['Europe', 'North Africa', 'western Asia']
	introducedDistribution = ['North America', 'eastern Africa', 'southern Africa', 'South America', 'Australia', 'New Zealand']
	habitat = 'In woodland'
	association = 'Ectomycorrhizal with broadleaf trees, rarely conifers'
	growthForm = 'On ground, singly or in troops or rings'
	abundance = 'Common'
	sporeColor = 'White'
	edibility = 'Poisonous'
	height = 'Up to 6 in'
	capDiameter = 'Up to 5 in'

	deathCap = fungiClass.Fungi(commonName, latinName, family, nativeDistribution, introducedDistribution, habitat, association, growthForm, abundance, sporeColor, edibility, height, capDiameter)

	return deathCap

def createDestroyingAngel():
	commonName = 'Destroying Angel'
	latinName = 'Amanita virosa'
	family = 'Amanitaceae'
	nativeDistribution = ['North America', 'Europe', 'Central America', 'northern Asia']
	introducedDistribution = []
	habitat = 'In woodland'
	association = 'Ectomycorrhizal with broadleaf trees and conifers'
	growthForm = 'On ground, singly or in troops'
	abundance = 'Occasional'
	sporeColor = 'White'
	edibility = 'Poisonous'
	height = 'Up to 6 in'
	capDiameter = 'Up to 5 in'

	destroyingAngel = fungiClass.Fungi(commonName, latinName, family, nativeDistribution, introducedDistribution, habitat, association, growthForm, abundance, sporeColor, edibility, height, capDiameter)

	return destroyingAngel

def displayFungus(fungus):
	fungus.displayCommonName()
	fungus.displayLatinName()
	fungus.displayFamily()
	fungus.displayNativeDistribution()
	fungus.displayIntroducedDistribution()
	fungus.displayHabitat()
	fungus.displayAssociation()
	fungus.displayGrowthForm()
	fungus.displayAbundance()
	fungus.displaySporeColor()
	fungus.displayEdibility()
	fungus.displayHeight()
	fungus.displayCapDiameter()

	print('\n')

def main():
	print('\n')

	deathCap = createDeathCap()
	displayFungus(deathCap)

	destroyingAngel = createDestroyingAngel()
	displayFungus(destroyingAngel)

	

if __name__ == '__main__':
	main()