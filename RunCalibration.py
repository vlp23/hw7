import CalibrationSettings as CalibSets
import scipy.stats as stat
import CalibrationClasses as CalibClass
import SurvivalModelClasses as SurvivalCls


calibrated = CalibClass.Calibration()

calibrated.sample_posterior()

#Question 4

print('Estimate of survivaltime ({:.{prec}%} credible interval):'.format(1-CalibSets.ALPHA, prec=0),
      calibrated.get_mortality_estimate_credible_interval(CalibSets.ALPHA, 4))

#Question 5

import CalibrationClasses as Cls
import CalibrationSettings as P


# initialize a calibrated model
calibrated_model = Cls.CalibratedModel('CalibrationResults.csv')
# simulate the calibrated model
calibrated_model.simulate(P.NUM_SIM_COHORTS, P.SIM_POP_SIZE, P.TIME_STEPS)


# report mean and projection interval
print('Mean survival time and {:.{prec}%} projection interval:'.format(1 - P.ALPHA, prec=0),
      calibrated_model.get_mean_survival_time_proj_interval(P.ALPHA, deci=4))



