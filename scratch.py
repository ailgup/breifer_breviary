            box = DayHeader(date="Sunday", title="Week II")
            story.append(box)

            hour = HourHeader(hour="Evening Prayer I")
            story.append(hour)

            #s = SectionHeader(title="Psalmody")
            #psalm_split_correctly(s,story)
            a = Antiphon(antiphon=[("Ant.", "Your word, O Lord is the lantern to light our way, alleluia."),
                                   ("Advent:",
                                    "New City of Zion, let your heart sing for joy; see how humbly your king comes to save you."),
                                   ("Lent, 2nd Sunday:",
                                    "Jesus took Peter, James and his brother John and let them up a high mountain. There he was transfigured before them."),
                                   ("Lent Palm Sunday:",
                                    "Day after day I sat teaching you in the temple and you did not lay hands on me. Now you come to scourge me and lead me to the cross."),
                                   ("Easter, 6th Sunday:", "The man of truth welcomes the light, alleluia.")
                                   ])
            psalm_split_correctly(a, story)
            p = Psalm(verse="Psalm 119:105-112",
                      titles=["XIV (Nun)", "A Meditation on God's Law"],
                      summary="This is my commandment: that you should love one another",
                      summary_verse="(John 15:12)",
                      text="Your word is a lamp for my steps <br />and a light for my path.<br />I have sworn and have made up my mind <br />to obey your decrees.<br /><br />Lord, I am deeply afflicted: <br />by your word give me life.<br />Accept, Lord, the homage of my lips <br />and teach me your decrees.<br /><br />Though I carry my life in my hands, <br />I remember your law.<br />Though the wicked try to ensnare me <br />I do not stray from your precepts.<br /><br />Your will is my heritage for ever, <br />the joy of my heart.<br />I set myself to carry out your will <br />in fullness, for ever. Glory..."
                      )
            psalm_split_correctly(p, story)

            a = Antiphon(
                antiphon=[("Ant.", "When I see your face, O Lord, I shall know the fullness of joy, alleluia."),
                          ("Advent:",
                           "Have courage, all of you, lost and fearful; take heart and say: Our God will come to save us, alleluia"),
                          ("Lent, 2nd Sunday:",
                           "Jesus took Peter, James and his brother John and let them up a high mountain. There he was transfigured before them."),
                          ("Lent Palm Sunday:",
                           "Day after day I sat teaching you in the temple and you did not lay hands on me. Now you come to scourge me and lead me to the cross."),
                          ("Easter, 6th Sunday:", "The man of truth welcomes the light, alleluia.")
                          ])
            psalm_split_correctly(a, story)
            p = Psalm(verse="Psalm 16",
                      titles=["The Lord himself is my heritage"],
                      summary="The Father raised up Jesus, freeing him from the grip of death",
                      summary_verse="Acts 2:24",
                      text='<p>Preserve me, God, I take refuge in you.<br />I say to you Lord "You are my God.<br />My happiness lies in you alone."<br /><br />You have put into my heart a marvelous love<br />for the faithful ones who dwell in your land.<br />Those who choose other gods increase their sorrows.<br />Never will I offer their offerings of blood.<br />Never will I take their name upon my lips.<br /><br />O Lord, it is you who are my portion and cup,<br />it is you yourself who are my prize.<br />The lot marked out for me is my delight,<br />welcome indeed the heritage that falls to me!<br /><br />I will bless the Lord who gives me counsel,<br />who even at night directs my heart.<br />I keep the Lord ever in my sight:<br />since he is at my right hand, I shall stand firm.<br /><br />And so my heart rejoices, my soul is glad;<br />even my body shall rest in safety.<br />For you will not leave my soul among the dead,<br />nor let your beloved know decay.<br /><br />You will show me the path of life,<br />the fullness of joy in your presence,<br />at your right hand happiness for ever. Glory...</p>'
                      )
            psalm_split_correctly(p, story)

            a = Antiphon(
                antiphon=[("Ant.", "Let everything in heaven and earth bend the knee at the name of Jesus, alleluia."),
                          ("Advent:",
                           "The law was given to Moses, but grace and truth come through Jesus Christ."),
                          ("Lent, 2nd Sunday:",
                           "Moses and Elijah were speaking to him of the death he would endure in Jerusalem."),
                          ("Lent Palm Sunday:",
                           "The Lord Jesus humbled himself by showing obedience even when this meant death, death on the cross."),
                          ("Easter, 6th Sunday:", "Let everything in heaven and earth bend the knee at the name of Jesus, alleluia.")
                          ])
            psalm_split_correctly(a, story)

            p = Psalm(verse="Canticle  -  Philippians 2:6-11",
                      titles=["Christ, God's holy servant"],
                      summary="",
                      summary_verse="",
                      text='Though he was in the form of God, <br />Jesus did not deem equality with God <br />something to be grasped at.<br /><br />Rather, he emptied himself <br />and took the form of a slave, <br />being born in the likeness of men.<br /><br />He was known to be of human estate, <br />and it was thus that he humbled himself,<br />obediently accepting even death, <br />death on a cross!<br /><br />Because of this, <br />God highly exalted him<br />and bestowed on him the name <br />above every other name,<br /><br />So that at Jesus&rsquo; name <br />every knee must bend<br />in the heavens, on the earth, <br />and under the earth,<br />and every tongue proclaim <br />to the glory of God the Father: <br />JESUS CHRIST IS LORD! Glory...'
                      )
            psalm_split_correctly(p, story)

            # reading
            r = Reading(book="Colossians", verse="1:2b-6a",
                        text="May God our Father give you grace and peace. We always give thanks to God, the Father of our Lord Jesus Christ, in our prayers for you because we have heard of your faith in Christ Jesus and the love you bear toward all the saints - moved as you are by the hope held in store for you in heaven. You heard of this hope through the message of truth, the gospel, which has come to you, has borne fruit, and has continued to grow in your midst, as it has everywhere in the world.")
            psalm_split_correctly(r, story)

            s = SectionHeader(title = "Magnificat")
            story.append(s)
            a = Antiphon(antiphon=[("Ant.","Behold the lamb of God, behold him who takes away the sins of the world.")])
            story.append(a)

            i = Intercessions(
                first="God aids and protects the people he has chosen for his inheritance.  Let us give thanks to him and proclaim his goodness:",
                response="Lord, we trust in you.",
                intercessions=[["We pray for N., our Pope, and N., our bishop,",
                                "protect them and in your goodness make them holy."],
                               ["May the sick feel their companionship with the suffering Christ,",
                                "and know that they will enjoy his eternal consolation."],
                               ["In your goodness have compassion on the homeless,",
                                "help them to find proper housing."],
                               ["In your goodness give and preserve the fruits of the earth,",
                                "so that each day there may be bread enough for all."],
                               ["Lord, you attend the dying with great mercy,", "grant them an eternal dwelling."]]
                )
            psalm_split_correctly(i, story)

            p=Prayer(prayers=["Almighty ever-living God,<br /> who govern all things,<br /> both in heaven and on earth,<br /> mercifully hear the pleading of your people<br /> and bestow your peace on our times.<br /> Through our Lord Jesus Christ, your Son,<br /> who lives and reigns with you in the unity of the Holy Spirit,<br /> God, for ever and ever."])
            story.append(p) #want to keep title togethert