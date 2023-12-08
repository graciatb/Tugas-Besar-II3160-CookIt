import React, { useState } from 'react'
import {
    Flex,
    Text,
    IconButton,
    Divider,
    Avatar,
    Heading,
} from '@chakra-ui/react'
import {
    FiMenu,
    FiCalendar,
    FiUser,
} from 'react-icons/fi'
import { IoFastFoodOutline } from "react-icons/io5";
import NavItem from '../component/navitem'
import { Link } from '@chakra-ui/next-js'

export default function Sidebar() {
    const [navSize, changeNavSize] = useState("large");
    return (
        <Flex
            pos="relative"
            left="5"
            h="95vh"
            marginTop="2.5vh"
            boxShadow="0 4px 12px 0 rgba(0, 0, 0, 0.3)"
            borderRadius={navSize == "small" ? "15px" : "30px"}
            w={navSize == "small" ? "75px" : "200px"}
            flexDir="column"
            justifyContent="space-between"
            bg="white"
        >
            <Flex
                p="5%"
                flexDir="column"
                w="100%"
                alignItems={navSize == "small" ? "center" : "flex-start"}
                as="nav"
            >
                <IconButton
                    aria-label="none"
                    background="none"
                    mt={5}
                    _hover={{ background: 'none' }}
                    icon={<FiMenu />}
                    onClick={() => {
                        if (navSize == "small")
                            changeNavSize("large")
                        else
                            changeNavSize("small")
                    }}
                />
                <Link href='/dashboard' w="full">
                <NavItem navSize={navSize} icon={IoFastFoodOutline} title="Recipe" description="See all recipe and order the ingredients" active />
                </Link>
                <Link href='/order' w="full">
                <NavItem navSize={navSize} icon={FiCalendar} title="Order History" description="See your ingrdients order history" w="full" />
                </Link>
            </Flex>
            <Flex
                p="5%"
                flexDir="column"
                w="100%"
                alignItems={navSize == "small" ? "center" : "flex-start"}
                mb={4}
            >
                <Flex
                    p="5%"
                    flexDir="column"
                    w="100%"
                    alignItems={navSize == "small" ? "center" : "flex-start"}
                    mb={4}
                >
                    <Divider display={navSize == "small" ? "none" : "flex"} />
                    <Flex mt={4} align="center">
                        <Link href='/'>
                            <NavItem navSize={navSize} icon={FiUser} title="Log Out" description="Log out from your CookIt account" />
                        </Link>
                    </Flex>
                </Flex>
            </Flex>
        </Flex>
    )
}