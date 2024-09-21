# GYM_Apps_ALEAPP

This repository contains the forensic analysis of 10 Android applications used for gym access control, focusing on the extraction of digital artifacts, security vulnerabilities, and forensic insights. The analysis was conducted using various tools and methods, such as ALEAPP, MobSF, JADX, and ADB, resulting in the development of 110 ALEAPP modules.

## Project Overview

We performed a comprehensive forensic analysis of 10 Android applications for managing gym access control (entries/exits, class bookings, etc.). This repository documents the analysis and provides forensic modules to automate artifact extraction.

## Key Tools Used

- **ADB**: Android Debug Bridge was used to extract public and private data along with APK files from the applications.
- **ALEAPP**: Used for analyzing artifacts such as login credentials, access logs, and user details.
- **MobSF**: Mobile Security Framework used for security assessments like permissions analysis, hardcoded secrets, and vulnerability detection.
- **JADX**: A decompiler for analyzing the source code of the applications to detect plaintext secrets and QR code generation vulnerabilities.

## Analysed Applications

1. **App1 - Befit**  
   *Description: A gym management app with features including class booking, workout tracking, and gym access logs.*

2. **App2 - GHC Ginásios**  
   *Description: Manage gym memberships, track workouts, and book classes at GHC gyms.*

3. **App3 - Go Gym**  
   *Description: Provides access control and class booking for Go Gym members.*

4. **App4 - HL Health Club**  
   *Description: HL Health Club offers personalized fitness plans and class reservations.*

5. **App5 - JAF CLUB**  
   *Description: JAF CLUB app allows users to check-in, book classes, and access gym schedules.*

6. **App6 - LR Fitness**  
   *Description: LR Fitness app features gym access control, nutrition plans, and workout schedules.*

7. **App7 - Move**  
   *Description: Move app helps users book fitness classes and track their progress.*

8. **App8 - MYHCGYM**  
   *Description: A comprehensive gym app for managing memberships and class schedules at MYHCGYM.*

9. **App9 - NF**  
   *Description: NF app offers access control, class booking, and personalized workout plans.*

10. **App10 - Total Combat**  
   *Description: Total Combat gym app provides tools for managing classes, workouts, and gym access.*

## Forensic Modules

Below is a list of the forensic modules created for each app. These modules automate the extraction and analysis of specific artifacts from the applications.

### Modules Overview

1. **Module: RegistoEntradasSaidas**
   - Extracts the log of gym entries and exits, including user identifiers and timestamps.

2. **Module: AtletaAvaliacao**
   - Retrieves athlete evaluation data stored within the app, including assessment history.

3. **Module: AtletaCheckinNaAplicacao**
   - Extracts data on user check-ins, providing insight into gym access patterns.

4. **Module: AtletaHorarioAulas**
   - Extracts the schedule of classes and athlete enrollment, including detailed timing and session information.

5. **Module: AtletaPlanoAlimentar**
   - Retrieves the user's nutritional plan data, if available within the app.

6. **Module: AtletaPlanoAlimetarDetalhado**
   - Provides a detailed view of the athlete’s nutrition plan, including daily intake records.

7. **Module: AtletaReservaAulas**
   - Extracts the reservation details for gym classes, including user IDs and class timing.

8. **Module: SettingsDecifrados**
   - Decrypts and extracts app settings that may have sensitive information in plaintext.

9. **Module: Settings**
   - Retrieves general application settings and configurations used by the user.

10. **Module: DuvidasEnviadasSuporte**
    - Analyzes and extracts user queries sent to support, helping understand user interaction and app feedback.

11. **Module: DefinicoesDoAtleta**
    - Extracts the athlete's profile settings, including user preferences and configurations.

## Results
### App1 - App10 Modules

#### RegistoEntradasSaidas  
**Results:** Found entries and exits for all 10 applications (App1 - App10).

#### AtletaAvaliacao 
**Results:** Evaluations found for App1 - App7 and App9 - App10.

#### AtletaCheckinNaAplicacao  
**Results:** Data found only for App5.

#### AtletaHorarioAulas
**Results:** Class schedules found for App1 - App7 and App9 - App10.

#### AtletaPlanoAlimentar  
**Results:** Dietary plans found for App2, App3, App5 - App7, and App9 - App10.

#### AtletaPlanoAlimentarDetalhado  
**Results:** Detailed dietary information found for App1 - App7 and App9 - App10.

#### AtletaReservaAulas  
**Results:** Class reservations found only for App2 and App5.

#### SettingsDecifrados  
**Results:** Settings decrypted successfully for all 10 applications (App1 - App10).

#### Settings  
**Results:** Settings extracted for all 10 applications (App1 - App10).

#### DuvidasEnviadasSuporte  
**Results:** Support inquiries found for App2 and App7.

#### DefinicoesDoAtleta  
**Results:** Favorite exercises and other user preferences extracted for App1 - App7 and App9 - App10.

### Data Variations Across Applications
The results across the applications vary, especially in terms of the presence of user-generated content. Some applications have empty tables due to the absence of certain features. However, modules were designed to account for these cases to ensure a comprehensive analysis.

For more details on the dataset, please refer to the results in the generated reports after running the ALEAPP modules.

## Conclusion
This repository automates the forensic analysis of Android gym access control applications, highlighting security vulnerabilities and extracting relevant digital artifacts. It provides researchers and forensic experts with a comprehensive toolkit to analyze similar apps for digital evidence and security issues.

## License
This project is licensed under the GPLv3 License.
