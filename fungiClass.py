class Fungi:
	'Common base class for all fungi'

	def __init__(self, commonName, latinName, family, nativeDistribution, introducedDistribution, habitat, association, growthForm, abundance, sporeColor, edibility, height, capDiameter):
		self.commonName = commonName
		self.latinName = latinName
		self.family = family
		self.nativeDistribution = nativeDistribution
		self.introducedDistribution = introducedDistribution
		self.habitat = habitat
		self.association = association
		self.growthForm = growthForm
		self.abundance = abundance
		self.sporeColor = sporeColor
		self.edibility = edibility
		self.height = height
		self.capDiameter = capDiameter

	def displayCommonName(self):
		print('Common name: %s' % self.commonName)

	def displayLatinName(self):
		print('Latin name: %s' % self.latinName)

	def displayFamily(self):
		print('Family: %s' % self.family)

	def displayNativeDistribution(self):
		print('Native Distribution: %s' % self.nativeDistribution)

	def displayIntroducedDistribution(self):
		print('Introduced Distribution: %s' % self.introducedDistribution)

	def displayHabitat(self):
		print('Habitat: %s' % self.habitat)

	def displayAssociation(self):
		print('Association: %s' % self.association)

	def displayGrowthForm(self):
		print('Growth Form: %s' % self.growthForm)

	def displayAbundance(self):
		print('Abundance: %s' % self.abundance)

	def displaySporeColor(self):
		print('Spore Color: %s' % self.sporeColor)

	def displayEdibility(self):
		print('Edibility: %s' % self.edibility)

	def displayHeight(self):
		print('Height: %s' % self.height)

	def displayCapDiameter(self):
		print('Cap Diameter: %s' % self.capDiameter)

	def compareFungus(self, fungus1, fungus2):
		attributeList = [commonName, latinName, family, nativeDistribution, introducedDistribution, habitat, association, growthForm, abundance, sporeColor, edibility, height, capDiameter]
		attributeNameList = ['commonName', 'latinName', 'family', 'nativeDistribution', 'introducedDistribution', 'habitat', 'association', 'growthForm', 'abundance', 'sporeColor', 'edibility', 'height', 'capDiameter']
		enumerate attribute, i in attributeList:
			if fungus1.attribute != fungus2.attribute:
				print('The following are differences between %s and %s:' % fungus1, fungus2)
				print('%s %s: %s' % fungus1, attributeNameList[i], attribute)