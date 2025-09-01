from .db_models import Task, Project, Employee, Note, Priority, TasksEmployees
from datetime import datetime

projects = [
    Project(
        project_name="James Webb Space Telescope",
        start_date=datetime.strptime("1996-01-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2022-07-12", "%Y-%m-%d"),
        is_completed=True,
    ),
    Project(
        project_name="Chandrayaan-3 Lunar Mission",
        start_date=datetime.strptime("2019-01-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2023-08-23", "%Y-%m-%d"),
        is_completed=True,
    ),
    Project(
        project_name="ITER Fusion Reactor",
        start_date=datetime.strptime("2007-11-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2035-12-31", "%Y-%m-%d"),
        is_completed=False,
    ),
    Project(
        project_name="High Luminosity LHC Upgrade",
        start_date=datetime.strptime("2018-01-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2029-12-31", "%Y-%m-%d"),
        is_completed=False,
    ),
    Project(
        project_name="Venus Orbiter Mission",
        start_date=datetime.strptime("2022-01-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2028-12-31", "%Y-%m-%d"),
        is_completed=False,
    ),
    Project(
        project_name="Mars Sample Return Mission",
        start_date=datetime.strptime("2020-01-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2033-12-31", "%Y-%m-%d"),
        is_completed=False,
    ),
    Project(
        project_name="International Space Station",
        start_date=datetime.strptime("1998-11-20", "%Y-%m-%d"),
        end_date=datetime.strptime("2031-12-31", "%Y-%m-%d"),
        is_completed=False,
    ),
    Project(
        project_name="Artemis Moon Program",
        start_date=datetime.strptime("2017-01-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2028-12-31", "%Y-%m-%d"),
        is_completed=False,
    ),
]


tasks = [
    # Tasks for James Webb Space Telescope (id=1)
    Task(
        task_description="Mirror segment manufacturing",
        start_date=datetime.strptime("2004-01-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2011-12-31", "%Y-%m-%d"),
        priority=Priority.high_priority,
        project_id=1,
    ),
    Task(
        task_description="Sunshield deployment testing",
        start_date=datetime.strptime("2012-01-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2014-06-30", "%Y-%m-%d"),
        priority=Priority.high_priority,
        project_id=1,
    ),
    Task(
        task_description="Cryogenic vacuum testing",
        start_date=datetime.strptime("2017-05-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2017-11-30", "%Y-%m-%d"),
        priority=Priority.high_priority,
        project_id=1,
    ),
    Task(
        task_description="Launch preparation and integration",
        start_date=datetime.strptime("2021-09-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2021-12-25", "%Y-%m-%d"),
        priority=Priority.high_priority,
        project_id=1,
    ),
    # Tasks for Chandrayaan-3 Lunar Mission (id=2)
    Task(
        task_description="Lander propulsion system upgrade",
        start_date=datetime.strptime("2019-03-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2020-08-31", "%Y-%m-%d"),
        priority=Priority.high_priority,
        project_id=2,
    ),
    Task(
        task_description="Terrain mapping camera calibration",
        start_date=datetime.strptime("2020-09-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2021-02-28", "%Y-%m-%d"),
        priority=Priority.mid_priority,
        project_id=2,
    ),
    Task(
        task_description="Failure-based design analysis",
        start_date=datetime.strptime("2020-01-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2021-06-30", "%Y-%m-%d"),
        priority=Priority.high_priority,
        project_id=2,
    ),
    Task(
        task_description="Integrated thermal vacuum testing",
        start_date=datetime.strptime("2022-11-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2023-03-31", "%Y-%m-%d"),
        priority=Priority.high_priority,
        project_id=2,
    ),
    # Tasks for ITER Fusion Reactor (id=3)
    Task(
        task_description="Tokamak assembly phase completion",
        start_date=datetime.strptime("2020-07-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2025-12-31", "%Y-%m-%d"),
        priority=Priority.high_priority,
        project_id=3,
    ),
    Task(
        task_description="Cryoplant system commissioning",
        start_date=datetime.strptime("2022-01-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2024-06-30", "%Y-%m-%d"),
        priority=Priority.mid_priority,
        project_id=3,
    ),
    Task(
        task_description="Magnet power supply installation",
        start_date=datetime.strptime("2023-01-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2026-12-31", "%Y-%m-%d"),
        priority=Priority.high_priority,
        project_id=3,
    ),
    Task(
        task_description="First plasma operations preparation",
        start_date=datetime.strptime("2025-01-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2030-12-31", "%Y-%m-%d"),
        priority=Priority.high_priority,
        project_id=3,
    ),
    # Tasks for High Luminosity LHC Upgrade (id=4)
    Task(
        task_description="New superconducting magnet development",
        start_date=datetime.strptime("2018-01-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2024-12-31", "%Y-%m-%d"),
        priority=Priority.high_priority,
        project_id=4,
    ),
    Task(
        task_description="Crab cavity prototype testing",
        start_date=datetime.strptime("2019-06-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2022-12-31", "%Y-%m-%d"),
        priority=Priority.mid_priority,
        project_id=4,
    ),
    Task(
        task_description="Beam pipe vacuum system upgrade",
        start_date=datetime.strptime("2023-01-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2025-06-30", "%Y-%m-%d"),
        priority=Priority.high_priority,
        project_id=4,
    ),
    Task(
        task_description="Collimator system installation",
        start_date=datetime.strptime("2026-01-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2027-12-31", "%Y-%m-%d"),
        priority=Priority.high_priority,
        project_id=4,
    ),
    # Tasks for Venus Orbiter Mission (id=5)
    Task(
        task_description="Synthetic aperture radar development",
        start_date=datetime.strptime("2022-03-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2024-02-28", "%Y-%m-%d"),
        priority=Priority.high_priority,
        project_id=5,
    ),
    Task(
        task_description="High-temperature electronics testing",
        start_date=datetime.strptime("2023-01-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2024-06-30", "%Y-%m-%d"),
        priority=Priority.high_priority,
        project_id=5,
    ),
    Task(
        task_description="Orbital insertion maneuver planning",
        start_date=datetime.strptime("2025-01-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2026-12-31", "%Y-%m-%d"),
        priority=Priority.mid_priority,
        project_id=5,
    ),
    Task(
        task_description="Thermal protection system validation",
        start_date=datetime.strptime("2024-07-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2025-12-31", "%Y-%m-%d"),
        priority=Priority.high_priority,
        project_id=5,
    ),
    # Tasks for Mars Sample Return Mission (id=6)
    Task(
        task_description="Sample tube sealing mechanism testing",
        start_date=datetime.strptime("2020-06-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2022-03-31", "%Y-%m-%d"),
        priority=Priority.high_priority,
        project_id=6,
    ),
    Task(
        task_description="Mars ascent vehicle development",
        start_date=datetime.strptime("2021-01-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2025-12-31", "%Y-%m-%d"),
        priority=Priority.high_priority,
        project_id=6,
    ),
    Task(
        task_description="Earth return orbiter propulsion",
        start_date=datetime.strptime("2022-07-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2026-06-30", "%Y-%m-%d"),
        priority=Priority.high_priority,
        project_id=6,
    ),
    Task(
        task_description="Sample containment system design",
        start_date=datetime.strptime("2023-01-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2025-12-31", "%Y-%m-%d"),
        priority=Priority.mid_priority,
        project_id=6,
    ),
    # Tasks for International Space Station (id=7)
    Task(
        task_description="Solar array upgrade installation",
        start_date=datetime.strptime("2021-06-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2023-12-31", "%Y-%m-%d"),
        priority=Priority.high_priority,
        project_id=7,
    ),
    Task(
        task_description="Life support system maintenance",
        start_date=datetime.strptime("2020-01-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2031-12-31", "%Y-%m-%d"),
        priority=Priority.high_priority,
        project_id=7,
    ),
    Task(
        task_description="Commercial module integration",
        start_date=datetime.strptime("2024-01-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2028-12-31", "%Y-%m-%d"),
        priority=Priority.mid_priority,
        project_id=7,
    ),
    Task(
        task_description="Crew rotation mission planning",
        start_date=datetime.strptime("2000-10-31", "%Y-%m-%d"),
        end_date=datetime.strptime("2031-12-31", "%Y-%m-%d"),
        priority=Priority.high_priority,
        project_id=7,
    ),
    # Tasks for Artemis Moon Program (id=8)
    Task(
        task_description="SLS rocket core stage testing",
        start_date=datetime.strptime("2017-01-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2021-01-16", "%Y-%m-%d"),
        priority=Priority.high_priority,
        project_id=8,
    ),
    Task(
        task_description="Lunar lander human rating certification",
        start_date=datetime.strptime("2021-01-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2026-12-31", "%Y-%m-%d"),
        priority=Priority.high_priority,
        project_id=8,
    ),
    Task(
        task_description="Gateway station power module",
        start_date=datetime.strptime("2019-01-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2024-12-31", "%Y-%m-%d"),
        priority=Priority.high_priority,
        project_id=8,
    ),
    Task(
        task_description="Lunar space suit development",
        start_date=datetime.strptime("2017-01-01", "%Y-%m-%d"),
        end_date=datetime.strptime("2025-12-31", "%Y-%m-%d"),
        priority=Priority.mid_priority,
        project_id=8,
    ),
]

employees = [
    Employee(first_name="James", last_name="Wilson", salary=85000, is_working=True),
    Employee(first_name="Sarah", last_name="Chen", salary=92000, is_working=True),
    Employee(
        first_name="Michael", last_name="Rodriguez", salary=78000, is_working=True
    ),
    Employee(first_name="Emily", last_name="Johnson", salary=68000, is_working=False),
    Employee(first_name="David", last_name="Kim", salary=95000, is_working=True),
    Employee(first_name="Jessica", last_name="Martinez", salary=81000, is_working=True),
    Employee(first_name="Daniel", last_name="Brown", salary=72000, is_working=True),
    Employee(first_name="Olivia", last_name="Davis", salary=89000, is_working=True),
    Employee(
        first_name="Christopher", last_name="Garcia", salary=83000, is_working=True
    ),
    Employee(first_name="Sophia", last_name="Miller", salary=76000, is_working=True),
    Employee(first_name="Matthew", last_name="Anderson", salary=91000, is_working=True),
    Employee(first_name="Isabella", last_name="Thomas", salary=69000, is_working=False),
    Employee(first_name="Andrew", last_name="Jackson", salary=87000, is_working=True),
    Employee(first_name="Mia", last_name="White", salary=74000, is_working=True),
    Employee(first_name="Joshua", last_name="Harris", salary=98000, is_working=True),
    Employee(first_name="Charlotte", last_name="Martin", salary=82000, is_working=True),
    Employee(first_name="Ethan", last_name="Thompson", salary=71000, is_working=True),
    Employee(first_name="Amelia", last_name="Moore", salary=86000, is_working=True),
    Employee(first_name="Joseph", last_name="Taylor", salary=93000, is_working=True),
    Employee(first_name="Harper", last_name="Williams", salary=77000, is_working=False),
    Employee(first_name="Ryan", last_name="Clark", salary=84000, is_working=True),
    Employee(first_name="Evelyn", last_name="Lewis", salary=79000, is_working=True),
    Employee(
        first_name="Alexander", last_name="Robinson", salary=97000, is_working=True
    ),
    Employee(first_name="Abigail", last_name="Walker", salary=73000, is_working=True),
    Employee(first_name="William", last_name="Young", salary=90000, is_working=True),
    Employee(first_name="Elizabeth", last_name="King", salary=88000, is_working=True),
    Employee(first_name="Noah", last_name="Scott", salary=75000, is_working=True),
    Employee(first_name="Sofia", last_name="Green", salary=94000, is_working=True),
    Employee(first_name="James", last_name="Adams", salary=80000, is_working=False),
    Employee(first_name="Avery", last_name="Nelson", salary=85000, is_working=True),
    Employee(first_name="Logan", last_name="Carter", salary=92000, is_working=True),
    Employee(first_name="Ella", last_name="Mitchell", salary=78000, is_working=True),
    Employee(first_name="Benjamin", last_name="Perez", salary=68000, is_working=True),
    Employee(first_name="Scarlett", last_name="Roberts", salary=95000, is_working=True),
    Employee(first_name="Samuel", last_name="Turner", salary=81000, is_working=True),
    Employee(first_name="Grace", last_name="Phillips", salary=72000, is_working=False),
    Employee(first_name="Jackson", last_name="Campbell", salary=89000, is_working=True),
    Employee(first_name="Chloe", last_name="Parker", salary=83000, is_working=True),
    Employee(first_name="John", last_name="Evans", salary=76000, is_working=True),
    Employee(first_name="Victoria", last_name="Edwards", salary=91000, is_working=True),
    Employee(first_name="Luke", last_name="Collins", salary=69000, is_working=True),
    Employee(first_name="Madison", last_name="Stewart", salary=87000, is_working=True),
    Employee(first_name="Anthony", last_name="Sanchez", salary=74000, is_working=False),
    Employee(first_name="Lily", last_name="Morris", salary=98000, is_working=True),
    Employee(first_name="Isaac", last_name="Rogers", salary=82000, is_working=True),
    Employee(first_name="Hannah", last_name="Reed", salary=71000, is_working=True),
    Employee(first_name="Dylan", last_name="Cook", salary=86000, is_working=True),
    Employee(first_name="Aria", last_name="Morgan", salary=93000, is_working=True),
    Employee(first_name="Nathan", last_name="Bell", salary=77000, is_working=True),
    Employee(first_name="Aubrey", last_name="Murphy", salary=84000, is_working=False),
    Employee(first_name="Carter", last_name="Bailey", salary=79000, is_working=True),
    Employee(first_name="Zoe", last_name="Rivera", salary=97000, is_working=True),
    Employee(first_name="Julian", last_name="Cooper", salary=73000, is_working=True),
    Employee(
        first_name="Natalie", last_name="Richardson", salary=90000, is_working=True
    ),
    Employee(first_name="Liam", last_name="Cox", salary=88000, is_working=True),
    Employee(first_name="Leah", last_name="Howard", salary=75000, is_working=False),
    Employee(first_name="Gabriel", last_name="Ward", salary=94000, is_working=True),
    Employee(first_name="Addison", last_name="Torres", salary=80000, is_working=True),
    Employee(first_name="Jayden", last_name="Peterson", salary=85000, is_working=True),
    Employee(first_name="Lillian", last_name="Gray", salary=92000, is_working=True),
    Employee(first_name="Caleb", last_name="Ramirez", salary=78000, is_working=True),
    Employee(first_name="Nora", last_name="James", salary=68000, is_working=False),
    Employee(first_name="Mason", last_name="Watson", salary=95000, is_working=True),
    Employee(first_name="Riley", last_name="Brooks", salary=81000, is_working=True),
    Employee(first_name="Henry", last_name="Kelly", salary=72000, is_working=True),
    Employee(first_name="Savannah", last_name="Sanders", salary=89000, is_working=True),
    Employee(first_name="Owen", last_name="Price", salary=83000, is_working=True),
    Employee(
        first_name="Brooklyn", last_name="Bennett", salary=76000, is_working=False
    ),
    Employee(first_name="Wyatt", last_name="Wood", salary=91000, is_working=True),
    Employee(first_name="Peyton", last_name="Barnes", salary=69000, is_working=True),
    Employee(first_name="Sebastian", last_name="Ross", salary=87000, is_working=True),
    Employee(first_name="Stella", last_name="Henderson", salary=74000, is_working=True),
    Employee(
        first_name="Christian", last_name="Coleman", salary=98000, is_working=True
    ),
    Employee(first_name="Bella", last_name="Jenkins", salary=82000, is_working=False),
    Employee(first_name="Jack", last_name="Perry", salary=71000, is_working=True),
    Employee(first_name="Lucy", last_name="Powell", salary=86000, is_working=True),
    Employee(first_name="Jonathan", last_name="Long", salary=93000, is_working=True),
    Employee(first_name="Ellie", last_name="Patterson", salary=77000, is_working=True),
    Employee(first_name="Eli", last_name="Hughes", salary=84000, is_working=True),
    Employee(first_name="Hailey", last_name="Flores", salary=79000, is_working=False),
    Employee(
        first_name="Isaiah", last_name="Washington", salary=97000, is_working=True
    ),
    Employee(first_name="Violet", last_name="Butler", salary=73000, is_working=True),
    Employee(first_name="Hunter", last_name="Simmons", salary=90000, is_working=True),
]

notes = [
    # Employee 1 - 3 notes
    Note(
        note_info="Mirror alignment calibration completed successfully",
        employee_id=1,
        task_id=1,
    ),
    Note(
        note_info="Sunshield deployment test passed all criteria",
        employee_id=1,
        task_id=2,
    ),
    Note(
        note_info="Cryogenic testing revealed minor thermal issues",
        employee_id=1,
        task_id=3,
    ),
    # Employee 2 - 2 notes
    Note(
        note_info="Lander propulsion upgrade meeting specifications",
        employee_id=2,
        task_id=5,
    ),
    Note(
        note_info="Terrain camera calibration requires recalibration",
        employee_id=2,
        task_id=6,
    ),
    # Employee 3 - 3 notes
    Note(
        note_info="Thermal vacuum testing passed all requirements",
        employee_id=3,
        task_id=8,
    ),
    Note(
        note_info="Mirror segment manufacturing quality exceptional",
        employee_id=3,
        task_id=1,
    ),
    Note(
        note_info="Vacuum test results exceeded expectations", employee_id=3, task_id=3
    ),
    # Employee 4 - 0 notes (not working)
    # Employee 5 - 3 notes
    Note(note_info="Tokamak assembly phase one on track", employee_id=5, task_id=9),
    Note(
        note_info="Cryoplant commissioning delayed two weeks", employee_id=5, task_id=10
    ),
    Note(
        note_info="Magnet power supply installation progressing well",
        employee_id=5,
        task_id=11,
    ),
    # Employee 6 - 2 notes
    Note(
        note_info="New magnet development meeting all specs", employee_id=6, task_id=13
    ),
    Note(
        note_info="Crab cavity prototype testing successful", employee_id=6, task_id=14
    ),
    # Employee 7 - 3 notes
    Note(note_info="Beam pipe upgrade design finalized", employee_id=7, task_id=15),
    Note(
        note_info="Collimator installation planning underway", employee_id=7, task_id=16
    ),
    Note(note_info="Magnet quench protection system tested", employee_id=7, task_id=13),
    # Employee 8 - 3 notes
    Note(note_info="SAR development proceeding as planned", employee_id=8, task_id=17),
    Note(
        note_info="High-temperature electronics test successful",
        employee_id=8,
        task_id=18,
    ),
    Note(
        note_info="Orbital insertion maneuver plan approved", employee_id=8, task_id=19
    ),
    # Employee 9 - 3 notes
    Note(
        note_info="Thermal protection validation completed successfully",
        employee_id=9,
        task_id=20,
    ),
    Note(
        note_info="Radar calibration needs additional work", employee_id=9, task_id=17
    ),
    Note(
        note_info="Heat shield material performing excellently",
        employee_id=9,
        task_id=20,
    ),
    # Employee 10 - 0 notes (not working)
    # Employee 11 - 3 notes
    Note(note_info="Sample tube sealing mechanism working", employee_id=11, task_id=21),
    Note(note_info="Mars ascent vehicle design finalized", employee_id=11, task_id=22),
    Note(
        note_info="Earth return orbiter propulsion tested", employee_id=11, task_id=23
    ),
    # Employee 12 - 2 notes
    Note(
        note_info="Solar array upgrade installation complete",
        employee_id=12,
        task_id=25,
    ),
    Note(
        note_info="Life support maintenance performed successfully",
        employee_id=12,
        task_id=26,
    ),
    # Employee 13 - 3 notes
    Note(note_info="Commercial module integration on hold", employee_id=13, task_id=27),
    Note(
        note_info="Crew rotation mission planning finalized", employee_id=13, task_id=28
    ),
    Note(
        note_info="Oxygen generator requires replacement parts",
        employee_id=13,
        task_id=26,
    ),
    # Employee 14 - 3 notes
    Note(note_info="SLS core stage tests completed", employee_id=14, task_id=29),
    Note(note_info="Lunar lander human rating in progress", employee_id=14, task_id=30),
    Note(note_info="Gateway power module delivered", employee_id=14, task_id=31),
    # Employee 15 - 3 notes
    Note(
        note_info="Orion spacecraft uncrewed test successful",
        employee_id=15,
        task_id=29,
    ),
    Note(
        note_info="Moon rover design approved for production",
        employee_id=15,
        task_id=30,
    ),
    Note(
        note_info="Client demo received positive feedback", employee_id=15, task_id=17
    ),
    # Employee 16 - 3 notes
    Note(
        note_info="Documentation updated for latest changes", employee_id=16, task_id=21
    ),
    Note(note_info="Quality assurance tests all passed", employee_id=16, task_id=25),
    Note(note_info="Vendor delivery delayed by one week", employee_id=16, task_id=14),
    # Employee 17 - 3 notes
    Note(note_info="Maintenance scheduled for next month", employee_id=17, task_id=22),
    Note(note_info="Client requested additional features", employee_id=17, task_id=19),
    Note(note_info="Budget approved for next quarter", employee_id=17, task_id=23),
    # Employee 18 - 3 notes
    Note(
        note_info="Testing environment configured successfully",
        employee_id=18,
        task_id=30,
    ),
    Note(
        note_info="Security audit completed without issues", employee_id=18, task_id=31
    ),
    Note(note_info="Backup systems tested and verified", employee_id=18, task_id=32),
    # Employee 19 - 3 notes
    Note(
        note_info="Final review meeting scheduled for Friday",
        employee_id=19,
        task_id=16,
    ),
    Note(note_info="All deliverables submitted on time", employee_id=19, task_id=20),
    Note(
        note_info="Client satisfaction survey results excellent",
        employee_id=19,
        task_id=12,
    ),
    # Employee 20 - 0 notes
    # Employee 21 - 3 notes
    Note(
        note_info="Team building event scheduled next month", employee_id=21, task_id=15
    ),
    Note(note_info="New safety protocols implemented", employee_id=21, task_id=8),
    Note(
        note_info="Performance review completed successfully", employee_id=21, task_id=4
    ),
    # Employee 22 - 3 notes
    Note(
        note_info="Stakeholder meeting produced positive outcomes",
        employee_id=22,
        task_id=3,
    ),
    Note(
        note_info="Cost savings identified in budget review", employee_id=22, task_id=1
    ),
    Note(
        note_info="New compliance requirements implemented", employee_id=22, task_id=6
    ),
    # Employee 23 - 3 notes
    Note(
        note_info="Vendor performance evaluation completed", employee_id=23, task_id=11
    ),
    Note(
        note_info="Mirror coating process improved significantly",
        employee_id=23,
        task_id=1,
    ),
    Note(note_info="Sunshield material passed stress tests", employee_id=23, task_id=2),
    # Employee 24 - 2 notes
    Note(note_info="Lander software update deployed", employee_id=24, task_id=5),
    Note(note_info="Camera calibration algorithm improved", employee_id=24, task_id=6),
    # Employee 25 - 3 notes
    Note(note_info="Failure mode analysis completed", employee_id=25, task_id=7),
    Note(
        note_info="Thermal vacuum chamber maintenance done", employee_id=25, task_id=8
    ),
    Note(note_info="Tokamak magnetic field calibrated", employee_id=25, task_id=9),
    # Employee 26 - 3 notes
    Note(note_info="New magnet design approved", employee_id=26, task_id=13),
    Note(note_info="Crab cavity performance exceptional", employee_id=26, task_id=14),
    Note(note_info="Beam pipe material selected", employee_id=26, task_id=15),
    # Employee 27 - 3 notes
    Note(note_info="Collimator alignment completed", employee_id=27, task_id=16),
    Note(note_info="SAR antenna deployed successfully", employee_id=27, task_id=17),
    Note(note_info="High-temp electronics passed tests", employee_id=27, task_id=18),
    # Employee 28 - 3 notes
    Note(
        note_info="Sample collection protocol established", employee_id=28, task_id=21
    ),
    Note(note_info="Ascent vehicle fuel tested", employee_id=28, task_id=22),
    Note(note_info="Return orbiter navigation calibrated", employee_id=28, task_id=23),
    # Employee 29 - 0 notes
    # Employee 30 - 3 notes
    Note(note_info="Solar arrays producing expected power", employee_id=30, task_id=25),
    Note(note_info="Life support filters replaced", employee_id=30, task_id=26),
    Note(note_info="Commercial module specs finalized", employee_id=30, task_id=27),
    # Employee 31 - 3 notes
    Note(note_info="Space suit mobility improved", employee_id=31, task_id=32),
    Note(note_info="Mirror alignment software updated", employee_id=31, task_id=1),
    Note(note_info="Sunshield deployment mechanism refined", employee_id=31, task_id=2),
    # Employee 32 - 3 notes
    Note(note_info="Cryogenic test data analyzed", employee_id=32, task_id=3),
    Note(note_info="Launch procedures documented", employee_id=32, task_id=4),
    Note(note_info="Propulsion system efficiency increased", employee_id=32, task_id=5),
    # Employee 33 - 3 notes
    Note(note_info="Vacuum test chamber prepared", employee_id=33, task_id=8),
    Note(note_info="Tokamak assembly phase two planned", employee_id=33, task_id=9),
    Note(note_info="Cryoplant output meeting targets", employee_id=33, task_id=10),
    # Employee 34 - 0 notes
    # Employee 35 - 3 notes
    Note(note_info="Plasma ignition sequence tested", employee_id=35, task_id=12),
    Note(note_info="New magnet production started", employee_id=35, task_id=13),
    Note(note_info="Crab cavity installation scheduled", employee_id=35, task_id=14),
    # Employee 36 - 3 notes
    Note(note_info="High-temp circuit boards delivered", employee_id=36, task_id=18),
    Note(
        note_info="Orbital insertion parameters finalized", employee_id=36, task_id=19
    ),
    Note(note_info="Thermal protection coating applied", employee_id=36, task_id=20),
    # Employee 37 - 3 notes
    Note(note_info="Sample tube design optimized", employee_id=37, task_id=21),
    Note(note_info="Ascent vehicle weight reduced", employee_id=37, task_id=22),
    Note(
        note_info="Return orbiter fuel efficiency improved", employee_id=37, task_id=23
    ),
    # Employee 38 - 3 notes
    Note(note_info="Life support oxygen levels stable", employee_id=38, task_id=26),
    Note(note_info="Commercial module docking tested", employee_id=38, task_id=27),
    Note(note_info="Crew health monitoring implemented", employee_id=38, task_id=28),
    # Employee 39 - 0 notes
    # Employee 40 - 3 notes
    Note(note_info="Lander descent algorithm improved", employee_id=40, task_id=30),
    Note(note_info="Gateway power storage increased", employee_id=40, task_id=31),
    Note(note_info="Space suit life support tested", employee_id=40, task_id=32),
    # Employee 41 - 2 notes
    Note(
        note_info="Final system integration testing started", employee_id=41, task_id=3
    ),
    Note(note_info="Launch and deployment ops planned", employee_id=41, task_id=4),
    # Employee 42 - 3 notes
    Note(
        note_info="Robustness testing completed successfully", employee_id=42, task_id=7
    ),
    Note(note_info="Launch vehicle integration on schedule", employee_id=42, task_id=8),
    Note(note_info="Lunar surface ops analysis ongoing", employee_id=42, task_id=8),
    # Employee 43 - 3 notes
    Note(note_info="Superconducting magnets meeting specs", employee_id=43, task_id=11),
    Note(note_info="Site infrastructure work completed", employee_id=43, task_id=10),
    Note(note_info="First plasma prep ahead of schedule", employee_id=43, task_id=12),
    # Employee 44 - 2 notes
    Note(
        note_info="New collimators installed successfully", employee_id=44, task_id=16
    ),
    Note(note_info="Commissioning tests beginning soon", employee_id=44, task_id=16),
    # Employee 45 - 3 notes
    Note(
        note_info="Payload instrument finalization delayed", employee_id=45, task_id=17
    ),
    Note(note_info="Spacecraft bus manufacturing started", employee_id=45, task_id=18),
    Note(
        note_info="Launch rehearsals scheduled next month", employee_id=45, task_id=19
    ),
    # Employee 46 - 3 notes
    Note(
        note_info="Perseverance sample collection ongoing", employee_id=46, task_id=21
    ),
    Note(
        note_info="Sample retrieval lander design finalized", employee_id=46, task_id=22
    ),
    Note(
        note_info="Earth return orbiter development on track",
        employee_id=46,
        task_id=23,
    ),
    # Employee 47 - 3 notes
    Note(
        note_info="Crew rotation mission launched successfully",
        employee_id=47,
        task_id=28,
    ),
    Note(
        note_info="Scientific experiment ops proceeding well",
        employee_id=47,
        task_id=27,
    ),
    Note(
        note_info="System maintenance completed on schedule", employee_id=47, task_id=26
    ),
    # Employee 48 - 0 notes
    # Employee 49 - 3 notes
    Note(note_info="Orion test flight data analyzed", employee_id=49, task_id=29),
    Note(note_info="Lunar Gateway modules in production", employee_id=49, task_id=31),
    Note(
        note_info="Lunar landing systems tested successfully",
        employee_id=49,
        task_id=30,
    ),
    # Employee 50 - 2 notes
    Note(note_info="Final mirror inspection completed", employee_id=50, task_id=1),
    Note(
        note_info="Integrated testing revealed vibration issues",
        employee_id=50,
        task_id=8,
    ),
    # Employee 51 - 3 notes
    Note(note_info="Vacuum vessel installation beginning", employee_id=51, task_id=9),
    Note(note_info="Magnet stability tests completed", employee_id=51, task_id=11),
    Note(note_info="Plasma containment tests successful", employee_id=51, task_id=12),
    # Employee 52 - 3 notes
    Note(note_info="Beam pipe manufacturing begun", employee_id=52, task_id=15),
    Note(note_info="Collimator materials ordered", employee_id=52, task_id=16),
    Note(note_info="SAR imaging tests successful", employee_id=52, task_id=17),
    # Employee 53 - 3 notes
    Note(note_info="Containment system safety enhanced", employee_id=53, task_id=24),
    Note(note_info="Solar array deployment tested", employee_id=53, task_id=25),
    Note(note_info="Crew health monitoring implemented", employee_id=53, task_id=28),
    # Employee 54 - 2 notes
    Note(note_info="SLS stage separation successful", employee_id=54, task_id=29),
    Note(note_info="Lander descent algorithm improved", employee_id=54, task_id=30),
    # Employee 55 - 3 notes
    Note(note_info="Gateway power storage increased", employee_id=55, task_id=31),
    Note(note_info="Space suit life support tested", employee_id=55, task_id=32),
    Note(note_info="Mirror cleaning procedure established", employee_id=55, task_id=1),
    # Employee 56 - 0 notes
    # Employee 57 - 3 notes
    Note(note_info="Sunshield material inventory stocked", employee_id=57, task_id=2),
    Note(note_info="Cryogenic system maintenance completed", employee_id=57, task_id=3),
    Note(note_info="Launch countdown procedures finalized", employee_id=57, task_id=4),
    # Employee 58 - 3 notes
    Note(note_info="Propulsion system upgrade completed", employee_id=58, task_id=5),
    Note(
        note_info="Failure analysis identified improvements", employee_id=58, task_id=7
    ),
    Note(note_info="Thermal testing passed criteria", employee_id=58, task_id=8),
    # Employee 59 - 3 notes
    Note(note_info="Budget review meeting scheduled", employee_id=59, task_id=9),
    Note(note_info="Software update for camera system", employee_id=59, task_id=6),
    Note(note_info="Safety inspection passed successfully", employee_id=59, task_id=11),
    # Employee 60 - 2 notes
    Note(note_info="Team training session completed", employee_id=60, task_id=13),
    Note(note_info="Client demo positive feedback", employee_id=60, task_id=17),
    # Employee 61 - 3 notes
    Note(note_info="Documentation updated for changes", employee_id=61, task_id=21),
    Note(note_info="Quality assurance tests passed", employee_id=61, task_id=25),
    Note(note_info="Vendor delivery delayed", employee_id=61, task_id=14),
    # Employee 62 - 0 notes
    # Employee 63 - 3 notes
    Note(note_info="Emergency drill completed", employee_id=63, task_id=26),
    Note(note_info="New team members onboarded", employee_id=63, task_id=29),
    Note(
        note_info="Performance metrics exceeding expectations",
        employee_id=63,
        task_id=18,
    ),
    # Employee 64 - 3 notes
    Note(note_info="Maintenance scheduled next month", employee_id=64, task_id=22),
    Note(note_info="Client requested additional features", employee_id=64, task_id=19),
    Note(note_info="Budget approved next quarter", employee_id=64, task_id=23),
    # Employee 65 - 3 notes
    Note(note_info="Technical specifications updated", employee_id=65, task_id=27),
    Note(note_info="Testing environment configured", employee_id=65, task_id=30),
    Note(note_info="Security audit completed", employee_id=65, task_id=31),
    # Employee 66 - 2 notes
    Note(note_info="Backup systems tested", employee_id=66, task_id=32),
    Note(note_info="New protocol implemented", employee_id=66, task_id=24),
    # Employee 67 - 3 notes
    Note(note_info="System optimization completed", employee_id=67, task_id=28),
    Note(note_info="Final review meeting scheduled", employee_id=67, task_id=16),
    Note(note_info="All deliverables submitted", employee_id=67, task_id=20),
    # Employee 68 - 3 notes
    Note(note_info="Client satisfaction results excellent", employee_id=68, task_id=12),
    Note(note_info="Team building event scheduled", employee_id=68, task_id=15),
    Note(note_info="New safety protocols implemented", employee_id=68, task_id=8),
    # Employee 69 - 0 notes
    # Employee 70 - 3 notes
    Note(note_info="Performance review completed", employee_id=70, task_id=4),
    Note(note_info="Software patch deployed", employee_id=70, task_id=7),
    Note(note_info="Hardware upgrade completed", employee_id=70, task_id=10),
    # Employee 71 - 3 notes
    Note(note_info="Training materials updated", employee_id=71, task_id=5),
    Note(note_info="Emergency response plan tested", employee_id=71, task_id=2),
    Note(note_info="Stakeholder meeting positive outcomes", employee_id=71, task_id=3),
    # Employee 72 - 3 notes
    Note(note_info="Cost savings identified", employee_id=72, task_id=1),
    Note(
        note_info="New compliance requirements implemented", employee_id=72, task_id=6
    ),
    Note(note_info="System integration testing beginning", employee_id=72, task_id=9),
    # Employee 73 - 2 notes
    Note(
        note_info="Vendor performance evaluation completed", employee_id=73, task_id=11
    ),
    Note(note_info="Mirror coating process improved", employee_id=73, task_id=1),
    # Employee 74 - 3 notes
    Note(note_info="Sunshield material passed tests", employee_id=74, task_id=2),
    Note(note_info="Cryogenic cooling system optimized", employee_id=74, task_id=3),
    Note(note_info="Launch sequence simulation successful", employee_id=74, task_id=4),
    # Employee 75 - 3 notes
    Note(note_info="Lander software update deployed", employee_id=75, task_id=5),
    Note(note_info="Camera calibration algorithm improved", employee_id=75, task_id=6),
    Note(note_info="Failure mode analysis completed", employee_id=75, task_id=7),
    # Employee 76 - 0 notes
    # Employee 77 - 3 notes
    Note(note_info="Thermal vacuum chamber maintenance", employee_id=77, task_id=8),
    Note(note_info="Tokamak magnetic field calibrated", employee_id=77, task_id=9),
    Note(note_info="Cryoplant efficiency improved", employee_id=77, task_id=10),
    # Employee 78 - 3 notes
    Note(note_info="Magnet cooling system upgraded", employee_id=78, task_id=11),
    Note(note_info="Plasma containment tests successful", employee_id=78, task_id=12),
    Note(note_info="New magnet design approved", employee_id=78, task_id=13),
    # Employee 79 - 3 notes
    Note(note_info="Crab cavity performance exceptional", employee_id=79, task_id=14),
    Note(note_info="Beam pipe material selected", employee_id=79, task_id=15),
    Note(note_info="Collimator alignment completed", employee_id=79, task_id=16),
    # Employee 80 - 2 notes
    Note(note_info="SAR antenna deployed successfully", employee_id=80, task_id=17),
    Note(note_info="High-temp electronics passed tests", employee_id=80, task_id=18),
    # Employee 81 - 3 notes
    Note(
        note_info="Orbital maneuver calculations verified", employee_id=81, task_id=19
    ),
    Note(note_info="Thermal shield installed", employee_id=81, task_id=20),
    Note(
        note_info="Sample collection protocol established", employee_id=81, task_id=21
    ),
    # Employee 82 - 3 notes
    Note(note_info="Ascent vehicle fuel tested", employee_id=82, task_id=22),
    Note(note_info="Return orbiter navigation calibrated", employee_id=82, task_id=23),
    Note(note_info="Containment system sterilized", employee_id=82, task_id=24),
    # Employee 83 - 0 notes
]

tasks_employees = [
    # Employee 1 - Works on JWST tasks
    TasksEmployees(task_id=1, employee_id=1),
    TasksEmployees(task_id=2, employee_id=1),
    TasksEmployees(task_id=3, employee_id=1),
    TasksEmployees(task_id=4, employee_id=1),
    # Employee 2 - Works on Chandrayaan-3 tasks
    TasksEmployees(task_id=5, employee_id=2),
    TasksEmployees(task_id=6, employee_id=2),
    TasksEmployees(task_id=7, employee_id=2),
    # Employee 3 - Works on JWST and Chandrayaan-3 tasks
    TasksEmployees(task_id=1, employee_id=3),
    TasksEmployees(task_id=3, employee_id=3),
    TasksEmployees(task_id=5, employee_id=3),
    TasksEmployees(task_id=8, employee_id=3),
    # Employee 4 - Not working (no tasks)
    # Employee 5 - Works on ITER tasks
    TasksEmployees(task_id=9, employee_id=5),
    TasksEmployees(task_id=10, employee_id=5),
    TasksEmployees(task_id=11, employee_id=5),
    TasksEmployees(task_id=12, employee_id=5),
    # Employee 6 - Works on HL-LHC tasks
    TasksEmployees(task_id=13, employee_id=6),
    TasksEmployees(task_id=14, employee_id=6),
    # Employee 7 - Works on HL-LHC tasks
    TasksEmployees(task_id=13, employee_id=7),
    TasksEmployees(task_id=15, employee_id=7),
    TasksEmployees(task_id=16, employee_id=7),
    # Employee 8 - Works on Venus Orbiter tasks
    TasksEmployees(task_id=17, employee_id=8),
    TasksEmployees(task_id=18, employee_id=8),
    TasksEmployees(task_id=19, employee_id=8),
    # Employee 9 - Works on Venus Orbiter tasks
    TasksEmployees(task_id=17, employee_id=9),
    TasksEmployees(task_id=20, employee_id=9),
    # Employee 10 - Not working (no tasks)
    # Employee 11 - Works on Mars Sample Return tasks
    TasksEmployees(task_id=21, employee_id=11),
    TasksEmployees(task_id=22, employee_id=11),
    TasksEmployees(task_id=23, employee_id=11),
    TasksEmployees(task_id=24, employee_id=11),
    # Employee 12 - Works on ISS tasks
    TasksEmployees(task_id=25, employee_id=12),
    TasksEmployees(task_id=26, employee_id=12),
    # Employee 13 - Works on ISS tasks
    TasksEmployees(task_id=26, employee_id=13),
    TasksEmployees(task_id=27, employee_id=13),
    TasksEmployees(task_id=28, employee_id=13),
    # Employee 14 - Works on Artemis tasks
    TasksEmployees(task_id=29, employee_id=14),
    TasksEmployees(task_id=30, employee_id=14),
    TasksEmployees(task_id=31, employee_id=14),
    TasksEmployees(task_id=32, employee_id=14),
    # Employee 15 - Works on Artemis and Venus tasks
    TasksEmployees(task_id=17, employee_id=15),
    TasksEmployees(task_id=29, employee_id=15),
    TasksEmployees(task_id=30, employee_id=15),
    # Employee 16 - Works on MSR and ISS tasks
    TasksEmployees(task_id=14, employee_id=16),
    TasksEmployees(task_id=21, employee_id=16),
    TasksEmployees(task_id=25, employee_id=16),
    TasksEmployees(task_id=26, employee_id=16),
    TasksEmployees(task_id=29, employee_id=16),
    # Employee 17 - Works on MSR and Venus tasks
    TasksEmployees(task_id=19, employee_id=17),
    TasksEmployees(task_id=22, employee_id=17),
    TasksEmployees(task_id=23, employee_id=17),
    # Employee 18 - Works on Artemis tasks
    TasksEmployees(task_id=24, employee_id=18),
    TasksEmployees(task_id=28, employee_id=18),
    TasksEmployees(task_id=30, employee_id=18),
    TasksEmployees(task_id=31, employee_id=18),
    TasksEmployees(task_id=32, employee_id=18),
    # Employee 19 - Works on HL-LHC, Venus, and ITER tasks
    TasksEmployees(task_id=12, employee_id=19),
    TasksEmployees(task_id=16, employee_id=19),
    TasksEmployees(task_id=20, employee_id=19),
    # Employee 20 - Not working (no tasks)
    # Employee 21 - Works on HL-LHC, Chandrayaan, JWST tasks
    TasksEmployees(task_id=2, employee_id=21),
    TasksEmployees(task_id=4, employee_id=21),
    TasksEmployees(task_id=5, employee_id=21),
    TasksEmployees(task_id=7, employee_id=21),
    TasksEmployees(task_id=8, employee_id=21),
    TasksEmployees(task_id=10, employee_id=21),
    TasksEmployees(task_id=15, employee_id=21),
    # Employee 22 - Works on JWST and Chandrayaan tasks
    TasksEmployees(task_id=1, employee_id=22),
    TasksEmployees(task_id=3, employee_id=22),
    TasksEmployees(task_id=6, employee_id=22),
    # Employee 23 - Works on JWST and ITER tasks
    TasksEmployees(task_id=1, employee_id=23),
    TasksEmployees(task_id=2, employee_id=23),
    TasksEmployees(task_id=3, employee_id=23),
    TasksEmployees(task_id=4, employee_id=23),
    TasksEmployees(task_id=11, employee_id=23),
    # Employee 24 - Works on Chandrayaan tasks
    TasksEmployees(task_id=5, employee_id=24),
    TasksEmployees(task_id=6, employee_id=24),
    # Employee 25 - Works on Chandrayaan and ITER tasks
    TasksEmployees(task_id=7, employee_id=25),
    TasksEmployees(task_id=8, employee_id=25),
    TasksEmployees(task_id=9, employee_id=25),
    TasksEmployees(task_id=10, employee_id=25),
    # Employee 26 - Works on HL-LHC tasks
    TasksEmployees(task_id=13, employee_id=26),
    TasksEmployees(task_id=14, employee_id=26),
    TasksEmployees(task_id=15, employee_id=26),
    # Employee 27 - Works on Venus and HL-LHC tasks
    TasksEmployees(task_id=16, employee_id=27),
    TasksEmployees(task_id=17, employee_id=27),
    TasksEmployees(task_id=18, employee_id=27),
    TasksEmployees(task_id=19, employee_id=27),
    TasksEmployees(task_id=20, employee_id=27),
    # Employee 28 - Works on MSR tasks
    TasksEmployees(task_id=21, employee_id=28),
    TasksEmployees(task_id=22, employee_id=28),
    TasksEmployees(task_id=23, employee_id=28),
    TasksEmployees(task_id=24, employee_id=28),
    # Employee 29 - Not working (no tasks)
    # Employee 30 - Works on ISS and Artemis tasks
    TasksEmployees(task_id=25, employee_id=30),
    TasksEmployees(task_id=26, employee_id=30),
    TasksEmployees(task_id=27, employee_id=30),
    TasksEmployees(task_id=28, employee_id=30),
    TasksEmployees(task_id=29, employee_id=30),
    TasksEmployees(task_id=30, employee_id=30),
    TasksEmployees(task_id=31, employee_id=30),
    # Employee 31 - Works on Artemis and JWST tasks
    TasksEmployees(task_id=1, employee_id=31),
    TasksEmployees(task_id=2, employee_id=31),
    TasksEmployees(task_id=32, employee_id=31),
    # Employee 32 - Works on JWST and Chandrayaan tasks
    TasksEmployees(task_id=3, employee_id=32),
    TasksEmployees(task_id=4, employee_id=32),
    TasksEmployees(task_id=5, employee_id=32),
    TasksEmployees(task_id=6, employee_id=32),
    TasksEmployees(task_id=7, employee_id=32),
    # Employee 33 - Works on ITER and Chandrayaan tasks
    TasksEmployees(task_id=8, employee_id=33),
    TasksEmployees(task_id=9, employee_id=33),
    TasksEmployees(task_id=10, employee_id=33),
    TasksEmployees(task_id=11, employee_id=33),
    # Employee 34 - Not working (no tasks)
    # Employee 35 - Works on ITER and HL-LHC tasks
    TasksEmployees(task_id=12, employee_id=35),
    TasksEmployees(task_id=13, employee_id=35),
    TasksEmployees(task_id=14, employee_id=35),
    TasksEmployees(task_id=15, employee_id=35),
    TasksEmployees(task_id=16, employee_id=35),
    TasksEmployees(task_id=17, employee_id=35),
    # Employee 36 - Works on Venus tasks
    TasksEmployees(task_id=18, employee_id=36),
    TasksEmployees(task_id=19, employee_id=36),
    TasksEmployees(task_id=20, employee_id=36),
    # Employee 37 - Works on MSR and ISS tasks
    TasksEmployees(task_id=21, employee_id=37),
    TasksEmployees(task_id=22, employee_id=37),
    TasksEmployees(task_id=23, employee_id=37),
    TasksEmployees(task_id=24, employee_id=37),
    TasksEmployees(task_id=25, employee_id=37),
    # Employee 38 - Works on ISS tasks
    TasksEmployees(task_id=26, employee_id=38),
    TasksEmployees(task_id=27, employee_id=38),
    TasksEmployees(task_id=28, employee_id=38),
    # Employee 39 - Not working (no tasks)
    # Employee 40 - Works on Artemis tasks
    TasksEmployees(task_id=30, employee_id=40),
    TasksEmployees(task_id=31, employee_id=40),
    TasksEmployees(task_id=32, employee_id=40),
    # Employee 41 - Works on JWST tasks
    TasksEmployees(task_id=3, employee_id=41),
    TasksEmployees(task_id=4, employee_id=41),
    # Employee 42 - Works on Chandrayaan tasks
    TasksEmployees(task_id=7, employee_id=42),
    TasksEmployees(task_id=8, employee_id=42),
    # Employee 43 - Works on ITER tasks
    TasksEmployees(task_id=10, employee_id=43),
    TasksEmployees(task_id=11, employee_id=43),
    TasksEmployees(task_id=12, employee_id=43),
    # Employee 44 - Works on HL-LHC tasks
    TasksEmployees(task_id=16, employee_id=44),
    # Employee 45 - Works on Venus tasks
    TasksEmployees(task_id=17, employee_id=45),
    TasksEmployees(task_id=18, employee_id=45),
    TasksEmployees(task_id=19, employee_id=45),
    # Employee 46 - Works on MSR tasks
    TasksEmployees(task_id=21, employee_id=46),
    TasksEmployees(task_id=22, employee_id=46),
    TasksEmployees(task_id=23, employee_id=46),
    # Employee 47 - Works on ISS tasks
    TasksEmployees(task_id=26, employee_id=47),
    TasksEmployees(task_id=27, employee_id=47),
    TasksEmployees(task_id=28, employee_id=47),
    # Employee 48 - Not working (no tasks)
    # Employee 49 - Works on Artemis tasks
    TasksEmployees(task_id=29, employee_id=49),
    TasksEmployees(task_id=30, employee_id=49),
    TasksEmployees(task_id=31, employee_id=49),
    # Employee 50 - Works on JWST and Chandrayaan tasks
    TasksEmployees(task_id=1, employee_id=50),
    TasksEmployees(task_id=8, employee_id=50),
    # Employee 51 - Works on ITER tasks
    TasksEmployees(task_id=9, employee_id=51),
    TasksEmployees(task_id=11, employee_id=51),
    TasksEmployees(task_id=12, employee_id=51),
    # Employee 52 - Works on HL-LHC and Venus tasks
    TasksEmployees(task_id=15, employee_id=52),
    TasksEmployees(task_id=16, employee_id=52),
    TasksEmployees(task_id=17, employee_id=52),
    # Employee 53 - Works on MSR and ISS tasks
    TasksEmployees(task_id=24, employee_id=53),
    TasksEmployees(task_id=25, employee_id=53),
    TasksEmployees(task_id=28, employee_id=53),
    # Employee 54 - Works on Artemis tasks
    TasksEmployees(task_id=29, employee_id=54),
    TasksEmployees(task_id=30, employee_id=54),
    # Employee 55 - Works on Artemis and JWST tasks
    TasksEmployees(task_id=1, employee_id=55),
    TasksEmployees(task_id=31, employee_id=55),
    TasksEmployees(task_id=32, employee_id=55),
    # Employee 56 - Not working (no tasks)
    # Employee 57 - Works on JWST tasks
    TasksEmployees(task_id=2, employee_id=57),
    TasksEmployees(task_id=3, employee_id=57),
    TasksEmployees(task_id=4, employee_id=57),
    # Employee 58 - Works on Chandrayaan tasks
    TasksEmployees(task_id=5, employee_id=58),
    TasksEmployees(task_id=7, employee_id=58),
    TasksEmployees(task_id=8, employee_id=58),
    # Employee 59 - Works on ITER and Chandrayaan tasks
    TasksEmployees(task_id=6, employee_id=59),
    TasksEmployees(task_id=9, employee_id=59),
    TasksEmployees(task_id=11, employee_id=59),
    # Employee 60 - Works on HL-LHC and Venus tasks
    TasksEmployees(task_id=13, employee_id=60),
    TasksEmployees(task_id=17, employee_id=60),
    # Employee 61 - Works on MSR and HL-LHC tasks
    TasksEmployees(task_id=14, employee_id=61),
    TasksEmployees(task_id=21, employee_id=61),
    TasksEmployees(task_id=25, employee_id=61),
    # Employee 62 - Not working (no tasks)
    # Employee 63 - Works on ISS and ITER tasks
    TasksEmployees(task_id=18, employee_id=63),
    TasksEmployees(task_id=26, employee_id=63),
    TasksEmployees(task_id=29, employee_id=63),
    # Employee 64 - Works on MSR and Venus tasks
    TasksEmployees(task_id=19, employee_id=64),
    TasksEmployees(task_id=22, employee_id=64),
    TasksEmployees(task_id=23, employee_id=64),
    # Employee 65 - Works on ISS and HL-LHC tasks
    TasksEmployees(task_id=27, employee_id=65),
    TasksEmployees(task_id=30, employee_id=65),
    TasksEmployees(task_id=31, employee_id=65),
    # Employee 66 - Works on MSR and Artemis tasks
    TasksEmployees(task_id=24, employee_id=66),
    TasksEmployees(task_id=32, employee_id=66),
    # Employee 67 - Works on HL-LHC and Venus tasks
    TasksEmployees(task_id=16, employee_id=67),
    TasksEmployees(task_id=20, employee_id=67),
    TasksEmployees(task_id=28, employee_id=67),
    # Employee 68 - Works on ITER and Chandrayaan tasks
    TasksEmployees(task_id=8, employee_id=68),
    TasksEmployees(task_id=12, employee_id=68),
    TasksEmployees(task_id=15, employee_id=68),
    # Employee 69 - Not working (no tasks)
    # Employee 70 - Works on JWST and ITER tasks
    TasksEmployees(task_id=4, employee_id=70),
    TasksEmployees(task_id=7, employee_id=70),
    TasksEmployees(task_id=10, employee_id=70),
    # Employee 71 - Works on Chandrayaan and JWST tasks
    TasksEmployees(task_id=2, employee_id=71),
    TasksEmployees(task_id=3, employee_id=71),
    TasksEmployees(task_id=5, employee_id=71),
    # Employee 72 - Works on JWST and ITER tasks
    TasksEmployees(task_id=1, employee_id=72),
    TasksEmployees(task_id=6, employee_id=72),
    TasksEmployees(task_id=9, employee_id=72),
    # Employee 73 - Works on ITER and JWST tasks
    TasksEmployees(task_id=1, employee_id=73),
    TasksEmployees(task_id=11, employee_id=73),
    # Employee 74 - Works on JWST tasks
    TasksEmployees(task_id=2, employee_id=74),
    TasksEmployees(task_id=3, employee_id=74),
    TasksEmployees(task_id=4, employee_id=74),
    # Employee 75 - Works on Chandrayaan tasks
    TasksEmployees(task_id=5, employee_id=75),
    TasksEmployees(task_id=6, employee_id=75),
    TasksEmployees(task_id=7, employee_id=75),
    # Employee 76 - Not working (no tasks)
    # Employee 77 - Works on ITER and Chandrayaan tasks
    TasksEmployees(task_id=8, employee_id=77),
    TasksEmployees(task_id=9, employee_id=77),
    TasksEmployees(task_id=10, employee_id=77),
    # Employee 78 - Works on ITER tasks
    TasksEmployees(task_id=11, employee_id=78),
    TasksEmployees(task_id=12, employee_id=78),
    TasksEmployees(task_id=13, employee_id=78),
    # Employee 79 - Works on HL-LHC tasks
    TasksEmployees(task_id=14, employee_id=79),
    TasksEmployees(task_id=15, employee_id=79),
    TasksEmployees(task_id=16, employee_id=79),
    # Employee 80 - Works on Venus tasks
    TasksEmployees(task_id=17, employee_id=80),
    TasksEmployees(task_id=18, employee_id=80),
    # Employee 81 - Works on Venus and MSR tasks
    TasksEmployees(task_id=19, employee_id=81),
    TasksEmployees(task_id=20, employee_id=81),
    TasksEmployees(task_id=21, employee_id=81),
    # Employee 82 - Works on MSR tasks
    TasksEmployees(task_id=22, employee_id=82),
    TasksEmployees(task_id=23, employee_id=82),
    TasksEmployees(task_id=24, employee_id=82),
    # Employee 83 - Not working (no tasks)
]
