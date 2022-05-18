import createReport as reporter
import enrollmentReservationQueries as enrollment
import assessmentQueries as assessment

#Updates SQL Server bulk insert csv for Capitol Hill program enrollment and housing reservations

def writeEnrollmentReservation(locations,reports):
    def generate(fileName, subfolder):
        reporter.prepareCSV(reporter.getQuery(enrollment.queries[fileName]),fileName,enrollment.savePaths[subfolder])
    
    for x in locations:
        for y in reports:
            reportName = x+y
            generate(reportName,x)
            print(reportName + " saved to " + enrollment.savePaths[x])

def writeAssessment():
    locations = assessment.locations
    for x in locations:
        saveLocation = assessment.getDestination(x)
        assessmentLocation = getattr(assessment,x)
        for y in assessmentLocation:
            assessmentName = y
            sql = assessmentLocation[y]
            reporter.prepareCSV(reporter.getQuery(sql),assessmentName,saveLocation)
            print(assessmentName + " saved to " + saveLocation)

writeEnrollmentReservation(enrollment.locationNames,enrollment.reportNames)
writeAssessment()