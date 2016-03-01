# This file contains all API version specific info.  Should only need editing
# for major changes in the OpenMM API.

# Add base classes missing from the XML input file
MISSING_BASE_CLASSES = {'OpenMMException':'std::exception'}

# Doc strings to replace some fo the confusing ones generaged by swig
# Indexed by (className, methodName)
DOC_STRINGS = {("Context", "setPositions") :
                "setPositions(self, positions)",
               ("Context", "setVelocities") :
                "setVelocities(self, velocities)"}

# Do not generate wrappers for the following methods.
# Indexed by (className, [methodName [, numParams]])
SKIP_METHODS = [('State',),
                ('Vec3',),
                ('AngleInfo',),
                ('ApplyAndersenThermostatKernel',),
                ('ApplyConstraintsKernel',),
                ('ApplyMonteCarloBarostatKernel',),
                ('BondInfo',),
                ('BondParameterInfo',),
                ('CalcAmoebaGeneralizedKirkwoodForceKernel',),
                ('CalcAmoebaAngleForceKernel',),
                ('CalcAmoebaBondForceKernel',),
                ('CalcAmoebaInPlaneAngleForceKernel',),
                ('CalcAmoebaMultipoleForceKernel',),
                ('CalcAmoebaOutOfPlaneBendForceKernel',),
                ('CalcAmoebaPiTorsionForceKernel',),
                ('CalcAmoebaStretchBendForceKernel',),
                ('CalcAmoebaTorsionTorsionForceKernel',),
                ('CalcAmoebaVdwForceKernel',),
                ('CalcAmoebaWcaDispersionForceKernel',),
                ('CalcCMAPTorsionForceKernel',),
                ('CalcCustomBondForceKernel',),
                ('CalcCustomCompoundBondForceKernel',),
                ('CalcCustomExternalForceKernel',),
                ('CalcCustomAngleForceKernel',),
                ('CalcCustomGBForceKernel',),
                ('CalcCustomHbondForceKernel',),
                ('CalcCustomNonbondedForceKernel',),
                ('CalcCustomTorsionForceKernel',),
                ('CalcForcesAndEnergyKernel',),
                ('CalcGBSAOBCForceKernel',),
                ('CalcHarmonicAngleForceKernel',),
                ('CalcHarmonicBondForceKernel',),
                ('CalcKineticEnergyKernel',),
                ('CalcNonbondedForceKernel',),
                ('CalcPeriodicTorsionForceKernel',),
                ('CalcRBTorsionForceKernel',),
                ('ComputationInfo',),
                ('ConstraintInfo',),
                ('CudaKernelFactory',),
                ('CudaStreamFactory',),
                ('ExceptionInfo',),
                ('ExclusionInfo',),
                ('FunctionInfo',),
                ('GlobalParameterInfo',),
                ('InitializeForcesKernel',),
                ('IntegrateBrownianStepKernel',),
                ('IntegrateLangevinStepKernel',),
                ('IntegrateVariableLangevinStepKernel',),
                ('IntegrateVariableVerletStepKernel',),
                ('IntegrateVerletStepKernel',),
                ('IntegrateCustomStepKernel',),
                ('Kernel',),
                ('KernelFactory',),
                ('KernelImpl',),
                ('MultipoleInfo',),
                ('OutOfPlaneBendInfo',),
                ('ParameterInfo',),
                ('ParticleInfo',),
                ('PeriodicTorsionInfo',),
                ('PerParticleParameterInfo',),
                ('PiTorsionInfo',),
                ('PlatformData',),
                ('RBTorsionInfo',),
                ('RemoveCMMotionKernel',),
                ('SplineFitter',),
                ('StreamFactory',),
                ('StretchBendInfo',),
                ('TorsionInfo',),
                ('TorsionTorsionGridInfo',),
                ('TorsionTorsionInfo',),
                ('UpdateStateDataKernel',),
                ('UpdateTimeKernel',),
                ('VdwInfo',),
                ('WcaDispersionInfo',),
                ('Context',  'getState'),
                ('Context',  'setState'),
                ('Context',  'createCheckpoint'),
                ('Context',  'loadCheckpoint'),
                ('CudaPlatform',),
                ('Force',    'Force'),
                ('ParticleParameterInfo',),
                ('Platform', 'createStream'),
                ('Platform', 'getDefaultStreamFactory'),
                ('Platform', 'registerStreamFactory'),
                ('Platform', 'contextCreated'),
                ('Platform', 'contextDestroyed'),
                ('Platform', 'createKernel'),
                ('Platform', 'registerKernelFactory'),
                ('IntegrateRPMDStepKernel',),
                ('RPMDIntegrator',  'getState'),
                ('CalcDrudeForceKernel',),
                ('IntegrateDrudeLangevinStepKernel',),
                ('IntegrateDrudeSCFStepKernel',),
                ('XmlSerializer',  'serialize'),
                ('XmlSerializer',  'deserialize'),
]

# The build script assumes method args that are non-const references are
# used to output values. This list gives excpetions to this rule.
NO_OUTPUT_ARGS = [('LocalEnergyMinimizer', 'minimize', 'context'),
                  ('System', 'getDefaultPeriodicBoxVectors', 'a'),
                  ('System', 'getDefaultPeriodicBoxVectors', 'b'),
                  ('System', 'getDefaultPeriodicBoxVectors', 'c'),
                  ('Platform', 'setPropertyValue', 'context'),
                  ('AmoebaTorsionTorsionForce', 'setTorsionTorsionGrid', 'grid'),
                  ('AmoebaVdwForce', 'setParticleExclusions', 'exclusions'),
                  ('AmoebaMultipoleForce', 'addParticle', 'molecularDipole'),
                  ('AmoebaMultipoleForce', 'addParticle', 'molecularQuadrupole'),
                  ('AmoebaMultipoleForce', 'setCovalentMap', 'covalentAtoms'),
                  ('AmoebaMultipoleForce', 'getElectrostaticPotential', 'context'),
                  ('AmoebaMultipoleForce', 'getInducedDipoles', 'context'),
]

# SWIG assumes the target language shadow class owns the C++ class
# so by default, when the  shadow class is deleted, the C++ class is also.
# However, if a class is passed to another class, it may be appropriate to
# change this.  The following dict lists the (Class,Methods) for which the
# shadow class should *lose* ownership of the C++ class.
# The list is the argument position(s).
STEAL_OWNERSHIP = {("Platform", "registerPlatform") : [0],
                   ("System", "addForce") : [0],
                   ("System", "setVirtualSite") : [1],
                   ("CustomNonbondedForce", "addTabulatedFunction") : [1],
                   ("CustomGBForce", "addTabulatedFunction") : [1],
                   ("CustomHbondForce", "addTabulatedFunction") : [1],
                   ("CustomCompoundBondForce", "addTabulatedFunction") : [1],
                   ("CustomManyParticleForce", "addTabulatedFunction") : [1],
                   ("CompoundIntegrator", "addIntegrator") : [0],
}


REQUIRE_ORDERED_SET = {("CustomNonbondedForce", "addInteractionGroup") : [0, 1],
                       ("CustomNonbondedForce", "setInteractionGroupParameters") : [1, 2],
}


# This is a list of units to attach to return values and method args.
# Indexed by (ClassName, MethodsName)
UNITS = {
("*", "getConstraintTolerance") : (None, ()),
("*", "getCutoffDistance") : ("unit.nanometers", ()),
("*", "getSwitchingDistance") : ("unit.nanometers", ()),
("*", "getDefaultCollisionFrequency") : ("1/unit.picosecond", ()),
("*", "getDefaultPeriodicBoxVectors")
 : (None, ('unit.nanometer', 'unit.nanometer', 'unit.nanometer')),
("*", "getDefaultPressure") : ("unit.bar", ()),
("*", "getDefaultPressureX") : ("unit.bar", ()),
("*", "getDefaultPressureY") : ("unit.bar", ()),
("*", "getDefaultPressureZ") : ("unit.bar", ()),
("*", "getDefaultSurfaceTension") : ("unit.bar*unit.nanometer", ()),
("*", "getDefaultTemperature") : ("unit.kelvin", ()),
("*", "getErrorTolerance") : (None, ()),
("*", "getEwaldErrorTolerance") : (None, ()),
("*", "getFriction") : ("1/unit.picosecond", ()),
("*", "getGlobalVariable") : (None, ()),
("*", "getGlobalVariableByName") : (None, ()),
("*", "getIntegrator") : (None, ()),
("*", "getMapParameters") : (None, ()),
("*", "getName") : (None, ()),
("*", "getNumAngles") : (None, ()),
("*", "getNumBonds") : (None, ()),
("*", "getNumPiTorsions") : (None, ()),
("*", "getNumConstraints") : (None, ()),
("*", "getNumExceptions") : (None, ()),
("*", "getNumForces") : (None, ()),
("*", "getNumMaps") : (None, ()),
("*", "getNumParticles") : (None, ()),
("*", "getNumPlatforms") : (None, ()),
("*", "getNumTorsions") : (None, ()),
("*", "getOpenMMVersion") : (None, ()),
("*", "getParticleMass") : ("unit.amu", ()),
("*", "getPlatform") : (None, ()),
("*", "getPlatformByName") : (None, ()),
("*", "getPluginLoadFailures"): (None, ()),
("*", "getRandomNumberSeed") : (None, ()),
("*", "getReactionFieldDielectric") : (None, ()),
("*", "getSoluteDielectric") : (None, ()),
("*", "getSolventDielectric") : (None, ()),
("*", "getStepSize") : ("unit.picosecond", ()),
("*", "getSystem") : (None, ()),
("*", "getTabulatedFunction") : (None, ()),
("*", "getUseDispersionCorrection") : (None, ()),
("*", "getTemperature") : ("unit.kelvin", ()),
("*", "getUseDispersionCorrection") : (None, ()),
("*", "getWeight") : (None, ()),
("*", "getWeight12") : (None, ()),
("*", "getWeight13") : (None, ()),
("*", "getWeightCross") : (None, ()),
("*", "getNonbondedMethod") : (None, ()),
("*", "getGlobalParameterDefaultValue") : (None, ()),
("*", "getPermutationMode") : (None, ()),
("LocalCoordinatesSite", "getOriginWeights") : (None, ()),
("LocalCoordinatesSite", "getXWeights") : (None, ()),
("LocalCoordinatesSite", "getYWeights") : (None, ()),
("LocalCoordinatesSite", "getLocalPosition") : ("unit.nanometer", ()),
("SerializationNode", "getChildren") : (None, ()),
("SerializationNode", "getChildNode") : (None, ()),
("SerializationNode", "getProperties") : (None, ()),
("SerializationNode", "getStringProperty") : (None, ()),
("SerializationNode", "getIntProperty") : (None, ()),
("SerializationNode", "getDoubleProperty") : (None, ()),
("SerializationProxy", "getProxy") : (None, ()),
("SerializationProxy", "getTypeName") : (None, ()),

# check getSurfaceAreaFactor
("AmoebaGeneralizedKirkwoodForce",       "getParticleParameters")                         :  (None, ('unit.elementary_charge', 'unit.nanometer', None)),
("AmoebaGeneralizedKirkwoodForce",       "getDielectricOffset")                           :  ( 'unit.nanometer', ()),
("AmoebaGeneralizedKirkwoodForce",       "getIncludeCavityTerm")                          :  ( None,()),
("AmoebaGeneralizedKirkwoodForce",       "getProbeRadius")                                :  ( 'unit.nanometer', ()),
("AmoebaGeneralizedKirkwoodForce",       "getSurfaceAreaFactor")                          :  ( 'unit.kilojoule_per_mole/(unit.nanometer*unit.nanometer)',()),

("AmoebaAngleForce",             "getAmoebaGlobalAngleCubic")             :  ( '1/unit.radian',()),
("AmoebaAngleForce",             "getAmoebaGlobalAngleQuartic")           :  ( '1/unit.radian**2',()),
("AmoebaAngleForce",             "getAmoebaGlobalAnglePentic")            :  ( '1/unit.radian**3',()),
("AmoebaAngleForce",             "getAmoebaGlobalAngleSextic")            :  ( '1/unit.radian**4',()),
("AmoebaAngleForce",             "getAngleParameters")                            :  ( None, (None, None, None, 'unit.degree', 'unit.kilojoule_per_mole/(unit.radian*unit.radian)')),

("AmoebaBondForce",              "getAmoebaGlobalBondCubic")              :  ( '1/unit.nanometer',()),
("AmoebaBondForce",              "getAmoebaGlobalBondQuartic")            :  ( '1/unit.nanometer**2',()),
("AmoebaBondForce",              "getBondParameters")                             :  ( None, (None, None, 'unit.nanometer', 'unit.kilojoule_per_mole/(unit.nanometer*unit.nanometer)')),

("AmoebaInPlaneAngleForce",      "getAmoebaGlobalInPlaneAngleCubic")      :  ( '1/unit.radian',()),
("AmoebaInPlaneAngleForce",      "getAmoebaGlobalInPlaneAngleQuartic")    :  ( '1/unit.radian**2',()),
("AmoebaInPlaneAngleForce",      "getAmoebaGlobalInPlaneAnglePentic")     :  ( '1/unit.radian**3',()),
("AmoebaInPlaneAngleForce",      "getAmoebaGlobalInPlaneAngleSextic")     :  ( '1/unit.radian**4',()),
("AmoebaInPlaneAngleForce",      "getAngleParameters")                            :  ( None, (None, None, None, None, 'unit.radian', 'unit.kilojoule_per_mole/(unit.radian*unit.radian)')),

("AmoebaMultipoleForce",                 "getNumMultipoles")                              :  ( None,()),
("AmoebaMultipoleForce",                 "getPolarizationType")                           :  ( None,()),
("AmoebaMultipoleForce",                 "getCutoffDistance")                             :  (  'unit.nanometer',()),
("AmoebaMultipoleForce",                 "getAEwald")                                     :  (  '1/unit.nanometer',()),
("AmoebaMultipoleForce",                 "getPmeBSplineOrder")                            :  ( None,()),
("AmoebaMultipoleForce",                 "getMutualInducedMaxIterations")                 :  ( None, ()),
("AmoebaMultipoleForce",                 "getMutualInducedTargetEpsilon")                 :  ( None, ()),
("AmoebaMultipoleForce",                 "getExtrapolationCoefficients")                            :  ( None, ()),
("AmoebaMultipoleForce",                 "getEwaldErrorTolerance")                        :  ( None, ()),
("AmoebaMultipoleForce",                 "getPmeGridDimensions")                          :  ( None,()),

# AmoebaMultipoleForce methods starting w/ getMultipoleParameters need work

# dipoleConversion        = AngstromToNm;
# quadrupoleConversion    = AngstromToNm*AngstromToNm;
# polarityConversion      = AngstromToNm*AngstromToNm*AngstromToNm;
# dampingFactorConversion = sqrt( AngstromToNm );

#    void getMultipoleParameters(int index, double& charge, std::vector<double>& molecularDipole, std::vector<double>& molecularQuadrupole,
#                                int& axisType, int& multipoleAtomZ, int& multipoleAtomX, int& multipoleAtomY, double& thole, double& dampingFactor, double& polarity ) const;
#    void getCovalentMap(int index, CovalentType typeId, std::vector<int>& covalentAtoms )
#    void getCovalentMaps(int index, std::vector < std::vector<int> >& covalentLists )

("AmoebaMultipoleForce",                 "getMultipoleParameters")                        :  ( None, ('unit.elementary_charge', 'unit.elementary_charge*unit.nanometer',
                                                                                                      'unit.elementary_charge*unit.nanometer**2', None, None, None, None, None, None,
                                                                                                      'unit.nanometer**3')),
("AmoebaMultipoleForce",                 "getCovalentMap")                                :  ( None, ()),
("AmoebaMultipoleForce",                 "getCovalentMaps")                               :  ( None, ()),
("AmoebaMultipoleForce",                 "getScalingDistanceCutoff")                      :  ( 'unit.nanometer', ()),
("AmoebaMultipoleForce",                 "getElectricConstant")                           :  ( None, ()),
#("AmoebaMultipoleForce",                 "getElectrostaticPotential")                     :  ( None, ('unit.kilojoule_per_mole')),
#("AmoebaMultipoleForce",                 "getElectrostaticPotential")                     :  ( ('unit.kilojoule_per_mole'), ()),
("AmoebaMultipoleForce",                 "getElectrostaticPotential")                     :  ( None, ()),
("AmoebaMultipoleForce",                 "getInducedDipoles")                             :  ( None, ()),
("AmoebaMultipoleForce",                 "getSystemMultipoleMoments")                     :  ( None, ()),

("AmoebaOutOfPlaneBendForce",            "getNumOutOfPlaneBends")                         :  ( None, ()),
("AmoebaOutOfPlaneBendForce",            "getAmoebaGlobalOutOfPlaneBendCubic")            :  ( '1/unit.radian',()),
("AmoebaOutOfPlaneBendForce",            "getAmoebaGlobalOutOfPlaneBendQuartic")          :  ( '1/unit.radian**2',()),
("AmoebaOutOfPlaneBendForce",            "getAmoebaGlobalOutOfPlaneBendPentic")           :  ( '1/unit.radian**3',()),
("AmoebaOutOfPlaneBendForce",            "getAmoebaGlobalOutOfPlaneBendSextic")           :  ( '1/unit.radian**4',()),
("AmoebaOutOfPlaneBendForce",            "getOutOfPlaneBendParameters")                   :  ( None, (None, None, None, None, 'unit.kilojoule_per_mole/unit.radians**2')),

("AmoebaPiTorsionForce",                  "getNumPiTorsions")                              :  ( None, ()),
("AmoebaPiTorsionForce",                  "getPiTorsionParameters")                        :  ( None, (None, None, None, None, None,  None, 'unit.kilojoule_per_mole')),

("AmoebaStretchBendForce",                "getNumStretchBends")                            :  ( None, ()),
("AmoebaStretchBendForce",                "getStretchBendParameters")                      :  ( None, (None, None, None, 'unit.nanometer', 'unit.nanometer', 'unit.radian', 'unit.kilojoule_per_mole/unit.nanometer/unit.radian', 'unit.kilojoule_per_mole/unit.nanometer/unit.radian')),

("AmoebaTorsionTorsionForce",             "getNumTorsionTorsions")                         :  ( None, ()),
("AmoebaTorsionTorsionForce",             "getNumTorsionTorsionGrids")                     :  ( None, ()),
("AmoebaTorsionTorsionForce",             "getTorsionTorsionParameters")                   :  ( None, ()),
("AmoebaTorsionTorsionForce",             "getTorsionTorsionGrid")                         :  ( None, ()),

# LPW 2012-10 : Is this a duplicate entry?
#("AmoebaVdwForce",                        "getParticleParameters")                         :  ( None, (None, None, None, 'unit.nanometer', 'unit.kilojoule_per_mole', None)),
("AmoebaVdwForce",                        "getSigmaCombiningRule")                         :  ( None, ()),
("AmoebaVdwForce",                        "getEpsilonCombiningRule")                       :  ( None, ()),
("AmoebaVdwForce",                        "getParticleExclusions")                         :  ( None, ()),
("AmoebaVdwForce",                        "getCutoff")                                     :  ( 'unit.nanometer', ()),
# LPW 2012-10 Modified because it no longer returns ivIndex and classIndex.
# ("AmoebaVdwForce",                        "getParticleParameters")                         :  ( None, (None, None, 'unit.nanometer', 'unit.kilojoule_per_mole', None)),
("AmoebaVdwForce",                        "getParticleParameters")                         :  ( None, (None, 'unit.nanometer', 'unit.kilojoule_per_mole', None,None)),

("AmoebaWcaDispersionForce",              "getParticleParameters")                         :  ( None, ('unit.nanometer', 'unit.kilojoule_per_mole')),
("AmoebaWcaDispersionForce",              "getAwater")                                     :  ( '1/(unit.nanometer*unit.nanometer*unit.nanometer)',()),
("AmoebaWcaDispersionForce",              "getDispoff")                                    :  ( 'unit.nanometer',()),
("AmoebaWcaDispersionForce",              "getRmino")                                      :  ( 'unit.nanometer',()),
("AmoebaWcaDispersionForce",              "getRminh")                                      :  ( 'unit.nanometer',()),
("AmoebaWcaDispersionForce",              "getEpso")                                       :  ( 'unit.kilojoule_per_mole',()),
("AmoebaWcaDispersionForce",              "getEpsh")                                       :  ( 'unit.kilojoule_per_mole',()),
("AmoebaWcaDispersionForce",              "getSlevy")                                      :  ( None, ()),
("AmoebaWcaDispersionForce",              "getShctd")                                      :  ( None, ()),

("Context", "getParameter") : (None, ()),
("Context", "getParameters") : (None, ()),
("Context", "getMolecules") : (None, ()),
("CMAPTorsionForce", "getMapParameters") : (None, (None, 'unit.kilojoule_per_mole')),
("CMAPTorsionForce", "getTorsionParameters") : (None, ()),
("CMMotionRemover", "getFrequency") : (None, ()),
("CustomAngleForce", "getNumPerAngleParameters") : (None, ()),
("CustomAngleForce", "getNumGlobalParameters") : (None, ()),
("CustomAngleForce", "getEnergyFunction") : (None, ()),
("CustomAngleForce", "getPerAngleParameterName") : (None, ()),
("CustomAngleForce", "getGlobalParameterName") : (None, ()),
("CustomAngleForce", "getAngleParameters") : (None, ()),
("CustomBondForce", "getNumPerBondParameters") : (None, ()),
("CustomBondForce", "getNumGlobalParameters") : (None, ()),
("CustomBondForce", "getEnergyFunction") : (None, ()),
("CustomBondForce", "getPerBondParameterName") : (None, ()),
("CustomBondForce", "getGlobalParameterName") : (None, ()),
("CustomBondForce", "getBondParameters") : (None, ()),
("CustomExternalForce", "getNumPerParticleParameters") : (None, ()),
("CustomExternalForce", "getNumGlobalParameters") : (None, ()),
("CustomExternalForce", "getEnergyFunction") : (None, ()),
("CustomExternalForce", "getPerParticleParameterName") : (None, ()),
("CustomExternalForce", "getGlobalParameterName") : (None, ()),
("CustomExternalForce", "getParticleParameters") : (None, ()),
("CustomGBForce", "getNumExclusions") : (None, ()),
("CustomGBForce", "getNumPerParticleParameters") : (None, ()),
("CustomGBForce", "getNumGlobalParameters") : (None, ()),
("CustomGBForce", "getNumFunctions") : (None, ()),
("CustomGBForce", "getNumComputedValues") : (None, ()),
("CustomGBForce", "getNumEnergyTerms") : (None, ()),
("CustomGBForce", "getPerParticleParameterName") : (None, ()),
("CustomGBForce", "getGlobalParameterName") : (None, ()),
("CustomGBForce", "getParticleParameters") : (None, ()),
("CustomGBForce", "getComputedValueParameters") : (None, ()),
("CustomGBForce", "getEnergyTermParameters") : (None, ()),
("CustomGBForce", "getExclusionParticles") : (None, ()),
("CustomGBForce", "getFunctionParameters") : (None, ()),
("CustomHbondForce", "getAcceptorParameters") : (None, ()),
("CustomHbondForce", "getDonorParameters") : (None, ()),
("CustomHbondForce", "getEnergyFunction") : (None, ()),
("CustomHbondForce", "getExclusionParticles") : (None, ()),
("CustomHbondForce", "getFunctionParameters") : (None, ()),
("CustomHbondForce", "getNumAcceptors") : (None, ()),
("CustomHbondForce", "getNumDonors") : (None, ()),
("CustomHbondForce", "getNumExclusions") : (None, ()),
("CustomHbondForce", "getNumFunctions") : (None, ()),
("CustomHbondForce", "getNumGlobalParameters") : (None, ()),
("CustomHbondForce", "getNumPerAcceptorParameters") : (None, ()),
("CustomHbondForce", "getNumPerDonorParameters") : (None, ()),
("CustomHbondForce", "getGlobalParameterName") : (None, ()),
("CustomHbondForce", "getPerAcceptorParameterName") : (None, ()),
("CustomHbondForce", "getPerDonorParameterName") : (None, ()),
("CustomNonbondedForce", "getEnergyFunction") : (None, ()),
("CustomNonbondedForce", "getExceptionParameters") : (None, ()),
("CustomNonbondedForce", "getExclusionParticles") : (None, ()),
("CustomNonbondedForce", "getFunctionParameters") : (None, ()),
("CustomNonbondedForce", "getGlobalParameterName") : (None, ()),
("CustomNonbondedForce", "getNumExclusions") : (None, ()),
("CustomNonbondedForce", "getNumFunctions") : (None, ()),
("CustomNonbondedForce", "getNumPerParticleParameters") : (None, ()),
("CustomNonbondedForce", "getNumParameters") : (None, ()),
("CustomNonbondedForce", "getNumGlobalParameters") : (None, ()),
("CustomNonbondedForce", "getParameterCombiningRule") : (None, ()),
("CustomNonbondedForce", "getParameterName") : (None, ()),
("CustomNonbondedForce", "getParticleParameters") : (None, ()),
("CustomNonbondedForce", "getPerParticleParameterName") : (None, ()),
("CustomTorsionForce", "getNumPerTorsionParameters") : (None, ()),
("CustomTorsionForce", "getNumGlobalParameters") : (None, ()),
("CustomTorsionForce", "getEnergyFunction") : (None, ()),
("CustomTorsionForce", "getPerTorsionParameterName") : (None, ()),
("CustomTorsionForce", "getGlobalParameterName") : (None, ()),
("CustomTorsionForce", "getTorsionParameters") : (None, ()),
("DrudeForce", "getParticleParameters") : (None, (None, None, None, None, None, 'unit.elementary_charge', 'unit.nanometer**3', None, None)),
("DrudeForce", "getNumScreenedPairs") : (None, ()),
("DrudeForce", "getScreenedPairParameters") : (None, ()),
("GBSAOBCForce", "getParticleParameters")
 : (None, ('unit.elementary_charge',
           'unit.nanometer', None)),
("GBSAOBCForce", "getSurfaceAreaEnergy") : ('unit.kilojoule_per_mole/unit.nanometer/unit.nanometer', ()),
("HarmonicAngleForce", "getAngleParameters")
 : (None, (None, None, None, 'unit.radian',
           'unit.kilojoule_per_mole/(unit.radian*unit.radian)')),
("HarmonicBondForce", "getBondParameters")
 : (None, (None, None, 'unit.nanometer',
           'unit.kilojoule_per_mole/(unit.nanometer*unit.nanometer)')),
("MonteCarloBarostat", "getFrequency") : (None, ()),
("MonteCarloAnisotropicBarostat", "getFrequency") : (None, ()),
("NonbondedForce", "getPMEParameters") : (None, ('1/unit.nanometer', None, None, None)),
("NonbondedForce", "getExceptionParameters")
 : (None, (None, None,
           'unit.elementary_charge*unit.elementary_charge',
           'unit.nanometer', 'unit.kilojoule_per_mole')),
("NonbondedForce", "getParticleParameters")
 : (None, ('unit.elementary_charge',
           'unit.nanometer', 'unit.kilojoule_per_mole')),
("PeriodicTorsionForce", "getTorsionParameters")
 : (None, (None, None, None, None,
           None, 'unit.radian', 'unit.kilojoule_per_mole')),
("Platform", "getDefaultPluginsDirectory") : (None, ()),
("Platform", "getPropertyDefaultValue") : (None, ()),
("Platform", "getPropertyNames") : (None, ()),
("Platform", "getPropertyValue") : (None, ()),
("Platform", "getSpeed") : (None, ()),
("RBTorsionForce", "getTorsionParameters")
 : (None, (None, None, None, None,
           'unit.kilojoules_per_mole', 'unit.kilojoules_per_mole', 'unit.kilojoules_per_mole',
           'unit.kilojoules_per_mole', 'unit.kilojoules_per_mole', 'unit.kilojoules_per_mole')),
("System", "getConstraintParameters") : (None, (None, None, 'unit.nanometer')),
("System", "getForce") : (None, ()),
("System", "getVirtualSite") : (None, ()),
("DrudeLangevinIntegrator", "getDrudeTemperature") : ("unit.kelvin", ()),
("DrudeLangevinIntegrator", "getMaxDrudeDistance") : ("unit.nanometer", ()),
("MonteCarloMembraneBarostat", "getXYMode") : (None, ()),
("MonteCarloMembraneBarostat", "getZMode") : (None, ()),
("DrudeLangevinIntegrator", "getDrudeFriction") : ("1/unit.picosecond", ()),
("DrudeSCFIntegrator", "getMinimizationErrorTolerance") : ("unit.kilojoules_per_mole/unit.nanometer", ()),
("RPMDIntegrator", "getContractions") : (None, ()),
("RPMDIntegrator", "getTotalEnergy") : ("unit.kilojoules_per_mole", ()),
}

